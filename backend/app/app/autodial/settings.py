# -*- coding: utf-8 -*-
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

import os

TG_API_URL = 'https://api.telegram.org'

SECRET_TOKEN = os.getenv('SECRET_TOKEN', 'not_secure')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')
