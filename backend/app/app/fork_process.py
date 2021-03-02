# -*- coding: utf-8 -*-
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

import asyncio
from concurrent.futures.process import ProcessPoolExecutor
from contextlib import suppress
from http import HTTPStatus
import json

import uvicorn
from fastapi import BackgroundTasks
from typing import Dict
from uuid import UUID, uuid4
from fastapi import FastAPI
from pydantic import BaseModel, Field

#from calc import cpu_bound_func
from app.autodial.autodial_apps import check_applications, ARIApp
from app.autodial.autodial_apps import create_and_maintain_channel

from app.config.custom_logging import CustomizeLogger
from pathlib import Path as Paths


config_path = Paths(__file__).parent.joinpath('config').joinpath("logging_config.json")
# print(f"config_path: {config_path}") ; import sys ; sys.exit()
logger = CustomizeLogger.make_logger(config_path)

# env_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 2)[0] + os.sep
env = Paths(__file__).parent.parent.joinpath('.env')
# print(f"env: {env}") ; import sys ; sys.exit()
#cpu_bound_func = ARIApp(env).connect(typeauto)

class Job(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    status: str = "in_progress"
    result: int = None


app = FastAPI()
jobs: Dict[UUID, Job] = {}


async def run_in_process(fn, *args):
    # asyncio.run_coroutine_threadsafe(ARIApp(env).connect(typeauto), loop=asyncio.get_running_loop())
    loop = asyncio.get_event_loop()
    logger.debug(f"start loop: {loop}")
    logger.exception(f"fn: {type(fn)}")
    fn_async = asyncio.run_coroutine_threadsafe(fn, loop=asyncio.get_running_loop())
    return await loop.run_in_executor(app.state.executor, fn_async, *args)  # wait and return result


async def start_cpu_bound_task(uid: UUID, param: int, typeauto: str) -> None:
    # jobs[uid].result = await run_in_process(cpu_bound_func, param) 374215\|374085
    jobs[uid].result = run_in_process(
    asyncio.run_coroutine_threadsafe(ARIApp(env).connect(typeauto), loop=asyncio.get_running_loop())
        , param)
    logger.info(f"jobs[uid].result: {jobs[uid].result}")
    jobs[uid].status = "complete"
    logger.info(f"jobs[uid].status: {jobs[uid].status}")


@app.post("/auto/new_ariapp_task/{param}", status_code=HTTPStatus.ACCEPTED)
async def task_handler(param: int, background_tasks: BackgroundTasks, typeauto: str):
    new_task = Job()
    jobs[new_task.uid] = new_task
    logger.info(f"start new_task: {new_task}")
    background_tasks.add_task(start_cpu_bound_task, new_task.uid, param, typeauto)
    return new_task


@app.get("/status/{uid}")
async def status_handler(uid: UUID):
    logger.info(f"Идентификатор задачи: {str(jobs[uid])}")
    return str(jobs[uid]).split(' '), {"data": uid}


@app.on_event("startup")
async def startup_event():
    app.state.executor = ProcessPoolExecutor()
    logger.info(f"startup_event: ")


@app.on_event("shutdown")
async def on_shutdown():
    app.state.executor.shutdown()
    logger.info(f"on_shutdown: ")


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        uvicorn.run("fork_process:app", host="0.0.0.0", port=8089, reload=True, log_level="info", debug=True)
