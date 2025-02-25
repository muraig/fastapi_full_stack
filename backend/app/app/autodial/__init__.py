# -*- coding: utf-8 -*-
"""
Программа для осуществлениия воспроизведения звуковых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

""" Создание подключения к Астериску """
""" Ожидание данных из сокета: await websocket.recv() """
""" Если статус канала StasisStart - принимаем вызов и воспроизводим голосовые файлы """

""" Получаем путь до файла csv со списком параметров клиентов """
""" Получаем список адресов в системе(ru/autodialer/1legal) голосовых файлов из функции checking_job_type """
""" Определение типа автообзвона и постановка задачи  """
"""
async def checking_job_type(phone, path_to_config_file, ev, ws_push, env_):
    Определение типа автообзвона и постановка задачи по их исполнению
    Возвращает список файлов для отправки задачи в Астериск, проверяя их наличие
    либо создавая с помощью сервера синтеза речи(RHVoice)
    с помощью метода:
    # list_sound = ReceivingCustomerData(phone, path_to_config_file, ws_push, env_)
    из класса: class ReceivingCustomerData:
    """

""" Получение данных о клиентах(контракт, долг) """
"""
class ReceivingCustomerData:
Класс для получения данных о клиентах
    Пока реализовано только получение из файла CSV
    # TODO Проверить необходимость получения данных из других источников
    # TODO: Сделат возможност выбора голосовых файлов для формирования типа автообзвона
    Класс возвращает шаблон для голосовы файлов(какие файлы в  какой тип автообзвона и их пути в системе)
    """
"""
    Получаем данные по клиентам из csv файла(из баз в дальнейшем)
    # TODO Сделать возможност получать данные из базы SQL
    """
"""
    Юрики
    """
"""
    Физики
    """
"""
    Физики с судом
    """
"""
    Летние водопроводы
    """
"""
    Метод для формирования автообзвона "Переход на прямые договора, начало месяца"
    # TODO: Не реализовано
    """
"""
    Метод для формирования автообзвона "Переход на прямые договора, конец месяца"
    # TODO: Не реализовано
    """

""" Создание(проверка наличия в системе) голосовых файлов контракта и долга """
"""
В функции:
    async def checking_job_type(phone, path_to_config_file, ev, ws_push, env_):
Из методов класса class ReceivingCustomerData:
    async def check_contract(self, phone, contract):
    async def check_dolg(self, phone, dolg):
    получаем имена(и пути) необходимых файлов контракта и долга для запуска в канал
С помощью класса: class CheckingAvailabilityCreatingContract:
    файлы проверяются на налиие либо создаются в файловой системе 

    """
