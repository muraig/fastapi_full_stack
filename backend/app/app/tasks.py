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

from app.celeryapp import app
from app.autodial.autodial_apps import check_applications, ARIApp

FILENAME = "/home/andrei/PycharmProjects/web_realtime_streaming/other/some_other_file.tsv"
env_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0] + os.sep
env = env_root + '.env'
# print(f"env: {env}") ; import sys ; sys.exit()

'''
import asyncio
from celery import Celery
app = Celery('tasks')
'''

async def async_function(typeauto):
    # more async stuff...
    await ARIApp(env).connect(typeauto)

@app.task(name='tasks.task_name', queue='queue_name')
def task_name(param1):
    asyncio.run(async_function(param1))


'''
async def async_task(typeauto):
    # await asyncio.sleep(42)
    await ARIApp(env).connect(typeauto)


@app.task
def regular_task(typeauto):
    coro = async_task(typeauto)
    asyncio.run(coro)
'''


'''
@app.task
async def start_app(typeauto):
    await ARIApp(env).connect(typeauto)
'''

'''
#from celery.decorators import task
from app.celeryapp import app


@app.task(name="sum_two_numbers")
def add(x, y):
    return x + y
'''
'''
import os

from app.celeryapp import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
'''

'''from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
'''
