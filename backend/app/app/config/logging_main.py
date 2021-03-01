# -*- coding: utf-8 -*-
"""
For logging test
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

from fastapi import FastAPI
from custom_logging import CustomizeLogger
from pathlib import Path
from fastapi import Request
import uvicorn
import logging

logger = logging.getLogger(__name__)

config_path = Path(__file__).parent.parent.joinpath('config').joinpath("logging_config.json")
# logger = CustomizeLogger.make_logger(config_path)

def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    return app


app = create_app()


@app.get('/custom-logger')
def customize_logger(request: Request):
    request.app.logger.info("Here Is Your Info Log")
    a = 1 / 0
    request.app.logger.error("Here Is Your Error Log")
    return {'data': "Successfully Implemented Custom Log"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8009)
