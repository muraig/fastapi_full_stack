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
from fastapi import FastAPI, UploadFile
import uuid
from typing import List


import asyncio


context = {'jobs': {}}

app = FastAPI()



async def do_work(job_key, files=None):
    iter_over = files if files else range(100)
    for file, file_number in enumerate(iter_over):
        jobs = context['jobs']
        job_info = jobs[job_key]
        job_info['iteration'] = file_number
        job_info['status'] = 'inprogress'
        await asyncio.sleep(1)
    pending_jobs[job_key]['status'] = 'done'


@app.post('/work/test')
async def testing(files: List[UploadFile]):
    identifier = str(uuid.uuid4())
    context[jobs][identifier] = {}
    asyncio.run_coroutine_threadsafe(do_work(identifier, files), loop=asyncio.get_running_loop())

    return {"identifier": identifier}


@app.get('/')
async def get_testing():
    identifier = str(uuid.uuid4())
    context['jobs'][identifier] = {}
    asyncio.run_coroutine_threadsafe(do_work(identifier), loop=asyncio.get_running_loop())

    return {"identifier": identifier}

@app.get('/status')
def status():
    return {
        'all': list(context['jobs'].values()),
    }

@app.get('/status/{identifier}')
async def status(identifier):
    return {
        "status": context['jobs'].get(identifier, 'job with that identifier is undefined'),
    }

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        uvicorn.run("0_fork_process:app", host="0.0.0.0", port=8089, reload=True, log_level="info", debug=True)
