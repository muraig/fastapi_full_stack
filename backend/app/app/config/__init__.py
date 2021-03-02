# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################
'''
from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Intro"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str
    DB_NAME: str


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    #

#settings = Settings()
settings = Settings(_env_file='/home/andrei/PycharmProjects/fastapi_full_stack/backend/app/.env', _env_file_encoding='utf-8')
print(f"DB_URL: {settings}") ; import sys ; sys.exit()
'''
