# -*- coding: utf-8 -*-
'''
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
'''
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

import subprocess
#from celery import app
#from tasks import pro
from contextlib import suppress

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        # Теперь вы можете запустить воркер, выполнив нашу программу с worker аргументом:
        # celery -A proj worker -l INFO
        # subprocess.call(['celery', '-A', 'app', 'worker', '--loglevel=INFO'])
        # celery multi start w1 -A proj -l INFO
        # celery multi stopwait w1 -A proj -l INFO
        #subprocess.run(['celery', 'multi', 'start', 'w1', '-A', 'app', '-l', 'INFO'])
        #subprocess.run(['celery', 'multi', 'restart', 'w1', '-A', 'app', '-l', 'INFO'])
        subprocess.run(['celery', 'multi', 'stopwait', 'w1', '-A', 'app', '-l', 'INFO'])
        # subprocess.run(['celery', 'worker', '-A', 'app.worker', '-l', 'info', '-Q', 'main-queue', '-c', '1'])
