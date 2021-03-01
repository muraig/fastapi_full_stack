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
from aiologger import Logger


async def main():
    logger = Logger.with_default_handlers(name='my-logger')

    await logger.debug("debug at stdout")
    await logger.info("info at stdout")

    await logger.warning("warning at stderr")
    await logger.error("error at stderr")
    await logger.critical("critical at stderr")

    await logger.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
