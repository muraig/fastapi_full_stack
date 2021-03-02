# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

import json
import os
from contextlib import suppress

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Request
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.autodial import fastapi_autodial as fastapi_auto_dial

from pydantic import BaseModel
from starlette.concurrency import run_until_first_complete
from starlette.routing import WebSocketRoute
from broadcaster import Broadcast
from fastapi.staticfiles import StaticFiles
############################################################
from app.config.custom_logging import CustomizeLogger
from pathlib import Path as Paths

import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
# from config import settings
from app.config.config import Settings

from apps.todo.routers import router as todo_router

env_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 2)[0] + os.sep
env = Paths(__file__).parent.parent.joinpath('.env')
# env = env_root + '.env'
# print(f"env: {env}") ; import sys ; sys.exit()

config_path = Paths(__file__).parent.joinpath('config').joinpath("logging_config.json")
logger = CustomizeLogger.make_logger(config_path)

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
# app = FastAPI(routes=routes, on_startup=[broadcast.connect], on_shutdown=[broadcast.disconnect], )
#########################################################

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
    routes=routes, on_startup=[broadcast.connect], on_shutdown=[broadcast.disconnect],
)
'''

def create_app() -> FastAPI:
    app = FastAPI(
        #title='CustomLogger', debug=False,
        title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
        routes=routes, on_startup=[broadcast.connect], on_shutdown=[broadcast.disconnect],
    )
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    return app


app = create_app()
'''

# монтирование статической папки для обслуживания статических файлов
add_path = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 0)[0]
# print(f"add_path: {add_path}")
os.chdir(add_path)
app.mount("/static", StaticFiles(directory="static"), name="static")

midlew = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS] ,\
         'http://192.168.1.97', 'http://127.0.0.1:8080', 'http://localhost:3000'
# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# logger.info(f"app.middleware(): {midlew}")
@app.post("/auto/push")
async def push_message(publish: Publish):
    """
    Я добавил маршрут веб-сокета в приложение FastAPI и публикую его в канале при каждом вызове API.
    """
    await broadcast.publish(publish.channel, json.dumps(publish.message))
    return Publish(channel=publish.channel, message=json.dumps(publish.message))


# sanity check route
@app.get('/auto/ping')
async def ping_pong(msg: str):
    """

    :param msg:
    :return:
    """
    # return {"ping": "pong"}
    # return jsonify('pong!')
    logger.info(f"ping: {msg}")
    return {msg: "pong!"}


########### from todo ######################
#app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    # Settings(_env_file=self.env, _env_file_encoding='utf-8').DATAFILE
    config = Settings(_env_file=env, _env_file_encoding='utf-8')
    # print(f"DB_URL: {config.DB_URL}")
    # print(f"DB_NAME: {config.DB_NAME}")
    app.mongodb_client = AsyncIOMotorClient(config.DB_URL)
    app.mongodb = app.mongodb_client[config.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(todo_router, tags=["tasks"], prefix="/task")

'''
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
'''

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(fastapi_auto_dial.auto_router)
'''
# logger.shutdown()
from starlette import status
from app.autodial import settings
from app.autodial.router import api_router
from app.autodial.utils import check_auth

docs_kwargs = {}  # noqa: pylint=invalid-name
if settings.ENVIRONMENT == 'production':
    docs_kwargs = dict(docs_url=None, redoc_url=None)  # noqa: pylint=invalid-name

app = FastAPI(**docs_kwargs)  # noqa: pylint=invalid-name


async def check_auth_middleware(request: Request):
    if settings.ENVIRONMENT in ('production', 'test'):
        body = await request.body()
        if not check_auth(body, request.headers.get('X-Hub-Signature', '')):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


app.include_router(api_router, dependencies=[Depends(check_auth_middleware)])
'''

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        #uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_level="info", debug=True)
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info", debug=True)

'/usr/local/bin/python /usr/local/bin/uvicorn --reload --host 0.0.0.0 --port 80 --log-level info app.main:app'
