# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################
import asyncio
import os
import json

#################################
import time
import uuid
from typing import Optional

from fastapi import Form
from fastapi import Request
from fastapi import APIRouter
from fastapi.params import Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from pydantic import BaseModel

from app.autodial.autodial_apps import check_applications
#, ARIApp
from app.autodial.autodial_apps import create_and_maintain_channel

from app.config.custom_logging import CustomizeLogger
from pathlib import Path as Paths

from typing import List

from fastapi import FastAPI, WebSocket
#, WebSocketDisconnect
from fastapi.websockets import WebSocketDisconnect
from fastapi.responses import HTMLResponse
# from fastapi.middleware.cors import CORSMiddleware


config_path = Paths(__file__).parent.parent.joinpath('config').joinpath("logging_config.json")
logger = CustomizeLogger.make_logger(config_path)

FILENAME = "/home/andrei/PycharmProjects/web_realtime_streaming/other/some_other_file.tsv"
env_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 2)[0] + os.sep
env = env_root + '.env'

add_path = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0]
os.chdir(add_path)
# print(f"add_path: {add_path}")
templates = Jinja2Templates(directory="templates")


auto_router = APIRouter()
#######################################################################
'''
from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
'''
#######################################################################
#######################################################################
''' Для создания вызова в Приложение автообзвона '''
@auto_router.get("/auto/phones/")
async def form_post(request: Request):
    """

    :param request:
    :return:
    """
    result = "Type a number"
    return templates.TemplateResponse('phone.html', context={'request': request, 'result': result})
''' Для просмотра созданных каналов в Stasis приложении '''
@auto_router.post("/auto/phones/")
async def form_post(request: Request, phone: int = Form(...)):
    """

    :param request:
    :param phone:
    :return:
    """
    global result
    typeautodial = ''
    # if phone == 4002 or phone == 4003 or phone == 4004 or 100 or 120:
    _time = str(time.time())
    _uniq = str(uuid.uuid4())
    ch_id = _time + '-' + _uniq
    result = await create_and_maintain_channel(typeautodial, phone, ch_id)
    # print(f"read_phones::result: {result.to_dict}")
    # print(f"read_phones::result: {(result.id, result.connected.number)}")
    logger.info(f"read_phones::result: {(result.id, result.connected.number)}")

    return templates.TemplateResponse('phone.html', context={'request': request, 'result': result})


''' Для создания типа автообзвона '''
@auto_router.get("/auto/form")
async def form_get_post(request: Request, phone: Optional[str] = Query(None, max_length=50)):
    """

    :param request:
    :param phone:
    :return:
    """
    req_text = await check_applications(env)
    # logger.info(f"form_get_post::req_text: {len(req_text[1])}")
    if len(req_text[1]) > 2:
        try:
            req = list(dict(json.loads(str(req_text[1])[1:-1])).items())
            rq = ';'.join([str(r) for r in req if not r[1] == []])
        except Exception as e:
            req_text = (200, '[{"name":"None","channel_ids":["None"]}]')
            req = list(dict(json.loads(str(req_text[1])[1:-1])).items())
            rq = ';'.join([str(r) for r in req if not r[1] == []])
            # print(f"{e}")
            logger.exception(f"{e}")
    else:
        req_text = (200, '[{"name":"None","channel_ids":["None"]}]')
        req = list(dict(json.loads(str(req_text[1])[1:-1])).items())
        rq = ';'.join([str(r) for r in req if not r[1] == []])
    # print(f"rq: {rq}")
    logger.info(f"rq: {rq}")
    return templates.TemplateResponse('form.html', context={'request': request, 'result': rq})
''' Для создания Stasis приложения '''
# Define your models here like
class model200(BaseModel):
    message: str = "Ok!"
class model404(BaseModel):
    message: str = "oppa..."
class model500(BaseModel):
    message: str = "mlya...."
@auto_router.post("/auto/form", responses={200: {"response": model200}, 404: {"response": model404}, 500: {"response": model500}})
async def form_post_post(request: Request, typeauto: str = Form(...)):
    """
    сделал запуск форком. теперь нужно отследить процесс для управления
    # TODO: сделал запуск форком. теперь нужно отследить процесс для управления
    :param request:
    :param typeauto:
    :return:
    """
    # id: str = Form(...), name: str = Form(...)
    #print(f"\nform_post::req: {typeauto}\n")

    from autodial_fork import get_date
    date = asyncio.run_coroutine_threadsafe(get_date(typeauto), loop=asyncio.get_running_loop())
    # print(f"Current date: {date}")
    logger.info(f"Current date: {date}")
    #date = asyncio.run(get_date())
    # выводим результат работы
    #print(f"Current date: {date}")

    await asyncio.sleep(0.1)
    req_text = await check_applications(env)
    # logger.info(f"form_get_post::req_text: {len(req_text[1])}")
    try:
        req = list(dict(json.loads(str(req_text[1])[1:-1])).items())
        rq = ';'.join([str(r) for r in req if not r[1] == []])
    except Exception as e:
        req_text = (200, '[{"name":"None","channel_ids":["None"]}]')
        req = list(dict(json.loads(str(req_text[1])[1:-1])).items())
        rq = ';'.join([str(r) for r in req if not r[1] == []])
        # print(f"{e}")
        logger.info(f"Exception: {e}")

    finally:
        await asyncio.sleep(0.1)
        logger.info(f"Current date: {'Ok!'}")

    return templates.TemplateResponse('form.html', context={'request': request, 'result': rq})



@auto_router.get("/auto/websocket")
async def form_post(request: Request):
    """

    :param request:
    :return:
    """
    result = "Type a number"
    return templates.TemplateResponse('websocket.html', context={'request': request, 'result': result})


@auto_router.post("/auto/websocket")
async def form_post(request: Request, num: int = Form(...)):
    """

    :param request:
    :param num:
    :return:
    """
    global result
    typeautodial = ''
    _time = str(time.time())
    _uniq = str(uuid.uuid4())
    ch_id = _time + '-' + _uniq
    result = await create_and_maintain_channel(typeautodial, num, ch_id)
    # print(f"read_phones::result: {(result.id, result.name)}")
    logger.info(f"read_phones::result: {(result.id, result.name)}")
    return templates.TemplateResponse('websocket.html', context={'request': request, 'result': result})
##################################################################################################
#######################################################################
#######################################################################
'''
from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from app.autodial.bot import proceed_release
from app.autodial.models import Body, Actions

api_router = APIRouter()  # noqa: pylint=invalid-name

@api_router.post("/release/")
async def release(*,
                  body: Body,
                  chat_id: str = None,
                  release_only: bool = False):

    if (body.release.draft and not release_only)             or body.action == Actions.released:
        res = await proceed_release(body, chat_id)
        return Response(status_code=res.status_code)
    return Response(status_code=status.HTTP_200_OK)
'''

########## chat ##########################
messages = []  # List of chat messages

# Class for connecting the client with the webSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message):
        for connection in self.active_connections:
            await connection.send_json(message)


manager = ConnectionManager()  # instance of the Connection Manager

# websocket for publish the comming message to all client connected in
@auto_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)  # connecting the client with the websocket
    try:
        while True:
            data = await websocket.receive_json()  # Data recieve when the client send a message
            messages.append(data)  # Add the coming message to the list of messages

            """ here we call a ConnectionManager method named "broadcast()" that publish the list of messages to
            all clients """
            await manager.broadcast(messages)

    except WebSocketDisconnect:
        manager.disconnect(websocket)  # deconnecting if an exeption handled
        # await manager.broadcast(messages)

'''
'''

