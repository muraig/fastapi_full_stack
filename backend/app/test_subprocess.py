# -*- coding: utf-8 -*-
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

import asyncio
import sys

async def get_date():
    # строка с кодом, которую будем выполнять,
    # ее можно заменить любой командой
    code = 'import datetime; print(datetime.datetime.now())'

    # Создаем подпроцесс и перенаправляем
    # стандартный вывод в канал `PIPE`.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Читаем вывод запущенной команды.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Ждем когда субпроцесс завершиться.
    await proc.wait()
    # возвращаем прочитанную строку
    return line

if __name__ == '__main__':
    date = asyncio.run(get_date())
    # выводим результат работы
    print(f"Current date: {date}")
