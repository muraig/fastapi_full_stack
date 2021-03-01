# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

from celery import Celery

# Первый аргумент Celery- это имя текущего модуля. Это необходимо только для того,
# чтобы имена могли автоматически генерироваться при определении задач в модуле __main__ .
celery_app = Celery("worker", broker="amqp://guest@queue//")

# Вы определили одну задачу под названием add, возвращающую сумму двух чисел.
# @app.task
# def add(x, y):
#     return x + y

celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}
