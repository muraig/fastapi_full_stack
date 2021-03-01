# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

#!/usr/bin/env python3

import sys

if sys.stdin.read(2) == 'a\n':
    sys.stdout.write('Good!\n')
else:
    sys.exit(1)

if sys.stdin.read(2) == 'b\n':
    sys.stdout.write('Wonderful!\n')
else:
    sys.exit(1)

sys.exit(0)