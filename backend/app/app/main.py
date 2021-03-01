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
'''
from aiologger import Logger
from app.config.custom_logging import CustomizeLogger
from pathlib import Path as Paths

logger = Logger.with_default_handlers(name='autodial')
#logger = logging.getLogger(__name__)
#config_path = Paths(__file__).with_name("logging_config.json")

log_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 0)[0] + '/config/'
config_path = log_root + "logging_config.json"
logger = CustomizeLogger.make_logger(config_path)
'''
'''
import logging

logging.basicConfig(level=logging.DEBUG, filename='autodial.log', format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
'''
'''
import logging.config

log_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0] + os.sep
# print(f"log_root: {log_root}") ; import sys ; sys.exit()
logging.config.fileConfig(log_root + 'logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

'''
'''
import logging.config
from pythonjsonlogger import jsonlogger
log_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0] + os.sep
logging.config.fileConfig(log_root + 'json_logging.ini', disable_existing_loggers=False)
#print(f"{__name__}: {log_root + 'json_logging.ini'}") ; import sys ; sys.exit()
logger = logging.getLogger(__name__)
'''
'''
import logging
from aiologger.loggers.json import JsonLogger
from aiologger.utils import CallableWrapper
from aiologger.handlers.files import AsyncFileHandler
from tempfile import NamedTemporaryFile

log_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0] + '/log/'
logger = JsonLogger.with_default_handlers(level=logging.DEBUG, flatten=True)
#temp_file = NamedTemporaryFile(errors=, buffering=1, encoding='utf8')
temp_file = NamedTemporaryFile(dir=log_root, )
# print(f"temp_file.name: {temp_file.name}") ; import sys ; sys.exit()
handler = AsyncFileHandler(filename=temp_file.name)
'''

import sys
import logging
from aiologger.loggers.json import JsonLogger
from aiologger.handlers.streams import AsyncStreamHandler

logger = JsonLogger.with_default_handlers(level=logging.DEBUG, flatten=True)
# handler = AsyncStreamHandler(stream=sys.stdout)

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

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


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
    await logger.info(f"ping: {msg}")
    return {msg: "pong!"}


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
        uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_level="info", debug=True)

'/usr/local/bin/python /usr/local/bin/uvicorn --reload --host 0.0.0.0 --port 80 --log-level info app.main:app'