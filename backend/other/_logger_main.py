# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

import logging
import string
import time
from contextlib import suppress
from random import random
import logging.config

import uvicorn
from fastapi import FastAPI
from fastapi import Request
from backend.app.services import EchoService

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response


@app.get("/")
async def root():
    logger.info("logging from the root logger")
    EchoService.echo("hi")
    return {"status": "alive"}

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        uvicorn.run("_logger_main:app", host="0.0.0.0", port=8765, reload=True, log_level="info", debug=True)
