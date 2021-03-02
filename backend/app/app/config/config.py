# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

from pydantic import BaseSettings, HttpUrl, DirectoryPath, IPvAnyAddress


class Settings(BaseSettings):
    SADDR: IPvAnyAddress
    URL: HttpUrl
    URLARI: HttpUrl
    URLAPPL: HttpUrl
    ARIUSER: str
    PASSW: str
    API_KEY: str
    PHONE1: int
    PHONE2: int
    R: HttpUrl
    API_ENDPOINT: HttpUrl
    WS_PUSH: HttpUrl
    DATAFILE: str
    STSPPS: str
    PATHF: DirectoryPath
    DB_URL: str
    DB_NAME: str


class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Intro"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str
    DB_NAME: str


'''
class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

'''
# config = Settings(_env_file='.env', _env_file_encoding='utf-8')
