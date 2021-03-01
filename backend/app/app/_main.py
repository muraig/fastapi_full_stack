# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""

from contextlib import suppress
import os

import uvicorn

from utils.app_exceptions import AppExceptionCase
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import fastapi_autodial
from autodial import fastapi_autodial as fastapi_auto_dial
from config.database import create_tables

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from utils.request_exceptions import (
    http_exception_handler,
    request_validation_exception_handler,
)
from utils.app_exceptions import app_exception_handler
import json

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from starlette.concurrency import run_until_first_complete
from starlette.routing import WebSocketRoute

from broadcaster import Broadcast


create_tables()

# app = FastAPI()

class Publish(BaseModel):
    """
    Class publish
    """
    channel: str = "lebowski"
    message: str
broadcast = Broadcast('memory://')
async def events_ws(websocket):
    """
    Мы определили две асинхронные функции для получения и публикации
    сообщений и передали их старлетке WebSocketRoute.
    Использовал Postgres как серверную часть для вещательной компании.
    async def events_ws(websocket):
    :rtype: object
    :param websocket:

    """
    await websocket.accept()
    await run_until_first_complete(
        (events_ws_receiver, {"websocket": websocket}),
        (events_ws_sender, {"websocket": websocket}),
    )
async def events_ws_receiver(websocket):
    """

    :param websocket: 
    """
    async for message in websocket.iter_text():
        await broadcast.publish(channel="events", message=message)
async def events_ws_sender(websocket):
    """

    :param websocket: 
    """
    async with broadcast.subscribe(channel="events") as subscriber:
        async for event in subscriber:
            await websocket.send_text(event.message)
routes = [
    WebSocketRoute("/events", events_ws, name="events_ws"),
]
"""
Теперь, когда мы определили маршрут веб-сокета с вещателем,
давайте просто добавим его FastAPI и заключим сделку.
"""
app = FastAPI(routes=routes, on_startup=[broadcast.connect], on_shutdown=[broadcast.disconnect], )

# монтирование статической папки для обслуживания статических файлов
add_path = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 0)[0]
# print(f"add_path: {add_path}")
os.chdir(add_path)
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://192.168.1.97",
    "http://192.168.1.97:8765",
    "ws://192.168.1.97:8765",
    "ws://192.168.1.97:8765/",
    "ws://192.168.1.97:8765/events",
    "http://localhost",
    "http://localhost:8765",
]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"], )
@app.post("/push")
async def push_message(publish: Publish):
    """
    Я добавил маршрут веб-сокета в приложение FastAPI и публикую его в канале при каждом вызове API.
    """
    await broadcast.publish(publish.channel, json.dumps(publish.message))
    return Publish(channel=publish.channel, message=json.dumps(publish.message))

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    """

    :param request: 
    :param e: 
    :return: 
    """
    return await http_exception_handler(request, e)
@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    """

    :param request: 
    :param e: 
    :return: 
    """
    return await request_validation_exception_handler(request, e)
@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    """

    :param request: 
    :param e: 
    :return: 
    """
    return await app_exception_handler(request, e)
app.include_router(fastapi_autodial.router)
app.include_router(fastapi_auto_dial.router)
@app.get("/")
async def root():
    """

    :return: 
    """
    return {"message": "Hello World"}


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        uvicorn.run("main:app", host="0.0.0.0", port=8765, reload=True, log_level="info", debug=True)
