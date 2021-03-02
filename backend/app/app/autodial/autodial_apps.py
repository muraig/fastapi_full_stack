# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

from __future__ import print_function

import os
import uuid
import json
from contextlib import suppress
from json.decoder import JSONDecodeError

import swagger_client
import uvicorn
from swagger_client.rest import ApiException

import aiofiles
import aiohttp as aiohttp
from aiocsv import AsyncDictReader
import websockets
import requests_async as requests

from app.config.config import Settings
import voicegen as vc

from app.config.custom_logging import CustomizeLogger
from pathlib import Path as Paths


config_path = Paths(__file__).parent.parent.joinpath('config').joinpath("logging_config.json")
logger = CustomizeLogger.make_logger(config_path)


# logger = Logger.with_default_handlers(name='autodial')
# logger = logging.getLogger(__name__)
# config_path = Paths(__file__).with_name("logging_config.json")

#logger = Logger.with_default_handlers(__name__)

# import logging
# logging.basicConfig(filename='autodial.log', format='%(process)d-%(levelname)s-%(message)s', level=logging.INFO)
# logging.basicConfig(filename='autodial.log', level=logging.DEBUG)
#     logger.debug("debug at stdout")
#     logger.info("info at stdout")
# 
#     logger.warning("warning at stderr")
#     logger.error("error at stderr")
#     logger.critical("critical at stderr")
# 
#     logger.shutdown()
#################################
# aiocsv.READ_SIZE = 2048
env_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 2)[0] + os.sep
env = env_root + '.env'
# print(f"env: {env}") ; import sys ; sys.exit()
FILENAME = env_root + "_filecsv.csv"

endpoint = ''


""" Создать вызов """
async def create_and_maintain_channel(typeautodial, _phone, _channel_id):
    """

    :param typeautodial:
    :param _phone:
    :param _channel_id:
    :return:
    """
    config = Settings(_env_file=env, _env_file_encoding='utf-8')
    configuration = swagger_client.Configuration()
    configuration.host = config.URLARI
    configuration.api_key['api_key'] = config.API_KEY

    async def create_channels_with_id(_phone, _channel_id):
        """

        :param _phone:
        :param _channel_id:
        :return:
        """
        # TODO endpoint - сделать правильно выбор в зависимости от типа звонков(местные, городские, сотовые)
        global endpoint
        api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
        if len(str(_phone)) <= 4:
            # print(f"create_channels_with_id::len(phone): {_phone} = {len(str(_phone))}")
            logger.info(f"|Длинна номера: {_phone}| = {len(str(_phone))}")
            endpoint = 'PJSIP/'
        elif len(str(_phone)) == 10:
            logger.info(f"|Длинна номера: {_phone}| = {len(str(_phone))}")
            endpoint = 'IAX2/Aster4_Aster1/'
        elif len(str(_phone)) == 11:
            logger.info(f"|Длинна номера: {_phone}| = {len(str(_phone))}")
            endpoint = 'IAX2/Aster4_Aster1/'

        endpoint += str(_phone)
        channel_id = _channel_id
        body = swagger_client.Containers()
        label = 'label_example'
        app = 'channel-playback'
        app_args = 'externalCall,' + typeautodial

        caller_id = _phone
        timeout = 60
        api_response = None
        try:
            api_response = api_instance.originate_with_id(endpoint, channel_id, body=body,
                                                          # extension=extension, context=context, priority=priority,
                                                          label=label, app=app, app_args=app_args,
                                                          caller_id=caller_id, timeout=timeout)
        except ApiException as e:
            # print("Exception when calling ChannelsApi->originate_with_id: %s\n" % e)
            logger.exception('exception')
        return api_response

    respone = await create_channels_with_id(_phone, _channel_id)
    # respone = ' '.join(respone)
    return respone


'''Получение данных из внешнего источника'''
async def async_receiving_customer_data(phone):
    """

    :param phone:
    :return:
    """
    # dict reading, tab-separated
    try:
        async with aiofiles.open(FILENAME, mode="r", encoding="utf-8", newline="") as afps:
            '''fieldnames = ["Клиент", "Phone", "Дата отправки на звонок", "Dolg", "Contract", "Результат",
                          "Число попыток Занято", "Число попыток Нет Ответа", "Результат ответа на звонок"]'''

            # file_reader = AsyncDictReader(afps, fieldnames=fieldnames, delimiter=";", dialect="unix")
            file_reader = AsyncDictReader(afps, delimiter=";", dialect="unix")
            csv_data = []
            async for row in file_reader:
                data_row = [row['Клиент'], row['Phone'], row['Дата отправки на звонок'], row['Dolg'], row['Contract'],
                            row['Результат'], row['Число попыток Занято'], row['Число попыток Нет Ответа'],
                            row['Результат ответа на звонок'], ]
                csv_data.append(data_row)
                # csv_data.append(row)

            """ Поиск по значению в csv файле """
            '''print('\n'.join([
                str(i) for i in csv_data if phone in str(i[1])
            ]))'''
            _receiving_customer_data = '\n'.join([str(i) for i in csv_data if phone in str(i[1])])
            # print(_receiving_customer_data)
            return _receiving_customer_data
    except FileNotFoundError as e:
        logger.exception(f"FileNotFoundError: {e}")
        return 0


'''Проверка сществования Stasis приложения'''
async def check_applications(_env):
    """

    :param _env: 
    :return: 
    """
    ws_appl = Settings(_env_file=_env, _env_file_encoding='utf-8').URLAPPL
    api_key = Settings(_env_file=_env, _env_file_encoding='utf-8').API_KEY
    headers = {
        'accept': '*/*',
    }
    params = (
        ('api_key', api_key),
    )
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ws_appl, headers=headers, params=params) as resp:
                code = resp.status
                appl_id = await resp.text()
                return code, appl_id
    except ConnectionError as er:
        # print(f'ConnectionError||: {er}')
        logger.exception(f'ConnectionError||: {er}')


'''Отправка данных в сопрограммы'''
async def curl_request(ws_push, ws_data=None, ev=None, ):
    """

    :param ws_push:
    :param ws_data:
    :param ev:
    :return:
    """
    # WS_PUSH=http://127.0.0.1:5050/push
    # self.ws_push, ws_data, ev
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json',
    }
    if ws_data is None:
        ev = f"\n{ev}\n"
    if ev is None:
        # print(f"ws_data: {ws_data} : {ev}")
        logger.info(f"ws_data: {ws_data} : {ev}")
    data = '{"channel":"events", "message":"' + str(ev) + '"}'
    # http://127.0.0.1:5050/push
    # print(f"curl_request:: ws_push: {ws_push}")
    # ws_push = 'http://127.0.0.1:8765/push'
    # ws_push = 'http://127.0.0.1:5050/push'
    # print(f"curl_request:: ws_push: {ws_push}")
    try:
        response = await requests.post(ws_push, headers=headers, data=data.encode('utf-8'))
        return response
    except ConnectionError as er:
        # print(f'ConnectionError||: {er}')
        logger.exception(f'ConnectionError||: {er}')


'''Проверка наличия и создание голосовых файлов'''
class CheckingAvailabilityCreatingContract:
    """
    Класс для формирования голосовых файлов
    """

    # noinspection PyArgumentList
    def __init__(self, phone, env_):
        self.phone = phone
        self.env = env_
        self.rhvoice = Settings(
            _env_file=self.env,
            _env_file_encoding='utf-8').R
        self.datafile = Settings(
            _env_file=self.env,
            _env_file_encoding='utf-8').DATAFILE
        self.pathf = Settings(
            _env_file=self.env,
            _env_file_encoding='utf-8').PATHF

    async def contr_validation(self, contract):
        """
        Создаем либо проверяем наличие звукового файла с номером contract
        :rtype: object
        :param contract:
        :return:
        """
        try:
            contract = int(contract)
        except Exception as e:
            # logging.error('Failed.', exc_info=e)
            # print(f"Error: {e}")
            logger.exception(f"Error: {e}")
            """ Убираем буквы из контракта, оставляем только цифры"""
            contract = ''.join([str(i) for i in contract if str.isdigit(i)])
        # TODO Переделать на асинхронную функцию vc.contract_to_worlds(contract)
        cont = vc.contract_to_worlds(contract)
        self.jsonc = await self.all_data_to_json(cont)
        self.jsoncs = str(self.jsonc).replace("'", '"')
        self.jsonc['file_path'] = self.jsonc['file_path'] + str(contract) + '.' + self.jsonc['format_']
        # print(f"self.jsonc.contract: {self.jsonc}")
        if not os.path.isfile(self.jsonc['file_path']):  # ''' Проверяем наличие файла '''
            # print(f"\nNOT: self.jsonc['file_path': {self.jsonc['file_path']}\n")
            logger.info(f"NOT: self.jsonc['file_path': {self.jsonc['file_path']}\n")
            await self.convert_text_to_file()  # ''' Запускаем процесс создания файла '''

        return contract

    async def dolg_validation(self, dolg):
        """
        Ищем в таблице по номеру телефона его сумму долга
        :param dolg:
        :return:
        """
        dolg = dolg.replace(",", '.')  # Получаем нужной структуры JSON
        # TODO Переделать на асинхронную функцию vc.contract_to_worlds(dolg)
        do = vc.float_to_worlds(dolg)
        self.jsonc = await self.all_data_to_json(do)
        # print(f"self.jsonc.dolg: {self.jsonc}")
        self.jsonc['file_path'] = self.jsonc['file_path'] + str(dolg) + '.' + self.jsonc['format_']
        if not os.path.isfile(self.jsonc['file_path']):
            # print(f"\nNOT: self.jsonc['file_path': {self.jsonc['file_path']}\n")
            logger.info(f"NOT: self.jsonc['file_path': {self.jsonc['file_path']}\n")
            await self.convert_text_to_file()  # Запускаем процесс создания файла

        return dolg

    async def all_data_to_json(self, text):
        """
        Формирование JSON стркты данных для исползования voicegen модля
        :param text:
        :return:
        """
        all_key = ('text', 'file_path', 'url', 'voice', 'format_', 'rate', 'pitch', 'volume')
        all_data_ = (text, str(self.pathf) + os.sep, str(self.rhvoice), 'anna', 'wav', 35, 25, 200)
        all_json_ = dict(zip(all_key, all_data_))

        return all_json_

    async def convert_text_to_file(self):
        """
        Создание голосовых файлов на основании переданного JSON запроса
        :return:
        """
        all_json = json.loads(self.jsoncs)
        output = vc.TTS(all_json)
        # TODO Переделать на асинхронную функцию vc.contract_to_worlds(save(all_json['file_path']))
        output.save(all_json['file_path'])
        # print(all_json['file_path'] + ' generated!')
        logger.info(all_json['file_path'] + ' generated!')

        return all_json['file_path']


'''Формирование структуры автообзвона, а также списка звуковых файлов'''
class ReceivingCustomerData:
    """
    Класс для получения данных о клиентах
    Пока реализовано только получение из файла CSV
    # TODO Проверить необходиомость получения данных из других источников

    """

    def __init__(self, phone, path_to_config_file, ws_push, env_):
        # TODO: Сделат возможност выбора голосовых файлов для формирования типа автообзвона
        self.legal = [
            'ru/autodialer/1legal',
            'autodial/',
            'ru/autodialer/2legal',
            'autodial/',
            'ru/autodialer/3legal']
        self.fizliz = [
            'ru/autodialer/1fizliz',
            'autodial/',
            'ru/autodialer/2fizliz',
            'autodial/',
            'ru/autodialer/3fizliz']
        self.fizlizcourt = [
            'ru/autodialer/1fizlizcourt',
            'autodial/',
            'ru/autodialer/2fizlizcourt',
            'autodial/',
            'ru/autodialer/3fizlizcourt']
        self.summer = [
            'ru/autodialer/1summer',
            'autodial/',
            'ru/autodialer/2summer', ]
        self.phone = phone
        self.pfile = path_to_config_file
        self.ws_push = ws_push
        # self.tt_monkeys = 'tt-monkeys'
        self.env = env_

    async def receiving_customer_data(self, ev=None):  # """ Подключаемся к базе данных? """
        """
        Полчаем данные по клиентам из csv файла(из баз в далнейем)
        # TODO Сделат возможност полчат данные из базы SQL
        :param ev:
        :return:
        """
        ws_data = self.phone
        try:
            await curl_request(self.ws_push, ws_data, ev)  # Отправка данных для мониторинга состояния вызова
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')
        """ Открываем файл.Создаем объект с данными из файла кусками(объем файла может быть большим)
        Ищем в таблице по номеру телефона его номер контракта
         """
        customer_data = await async_receiving_customer_data(self.phone)
        return customer_data

    async def legal_entities(self, ev):
        """
        Юрики
        :param ev:
        :return:
        """
        cus_data = await self.receiving_customer_data(ev)
        return self.legal, cus_data

    async def individuals(self, ev):
        """
        Физики
        :param ev:
        :return:
        """
        cus_data = await self.receiving_customer_data(ev)
        return self.fizliz, cus_data

    async def individuals_with_court(self, ev):
        """
        Физики с судом
        :param ev:
        :return:
        """
        cus_data = await self.receiving_customer_data(ev)
        return self.fizlizcourt, cus_data

    async def summer_water_supply(self, ev):
        """
        Летние водопроводы
        :param ev:
        :return:
        """
        cus_data = await self.receiving_customer_data(ev)
        return self.summer, cus_data

    def handover_start_month(self):
        """
        Метод для формирования автообзвона "Переход на прямые договора, начало месяца"
        # TODO: Не реализовано
        """
        return None

    def handover_end_month(self):
        """
        Метод для формирования автообзвона "Переход на прямые договора, конец месяца"
        # TODO: Не реализовано
        """
        return None

    async def check_contract(self, phone, contract):
        """
        Запскаем проесс создания звовых файлов
        :param contract:
        :param phone:
        :return:
        """
        c = CheckingAvailabilityCreatingContract(phone, self.env)
        text = await c.contr_validation(contract)
        return text

    async def check_dolg(self, phone, dolg):
        """
        Запскаем проесс создания звовых файлов
        :param dolg:
        :param phone:
        :return:
        """
        d = CheckingAvailabilityCreatingContract(phone, self.env)
        text = await d.dolg_validation(dolg)
        return text


''' Определение типа автообзвона и постановка задачи по их исполнению
    Возвращает список файлов для отправки задачи в Астериск'''
async def checking_job_type(phone, path_to_config_file, ev, ws_push, env_):
    """
    Создаем объект - класс с методами:
    При инициализации создаются внутренние переменные,
    запрашиваются данные из внешнего хранилища
    Сначала определся тип автообзвона:
        юрики, физики, физики с долгом, летний водопровод,
        рассылкаа о смене получателя платежа(начала месяца и конец месяца)
    По номеру телефона получаем параметры:
        Номер контракта
        Сумма долга(если обзвон с долгом)
    Возвращается из функции список с адресами звуковых файлов
    # TODO если для обзвона не хватает данных(нет номера контракта либо суммы долга) - вызов не производить!
    """
    jobe_type = ev['args'][1]

    list_sound = ReceivingCustomerData(phone, path_to_config_file, ws_push, env_)

    """ Определяем тип обзвона """
    if jobe_type in "urliz":
        urliz, cus_data = await list_sound.legal_entities(ev)
        # print(f"customer_data: {cus_data}")
        logger.info(f"customer_data: {cus_data}")
        # TODO Сделать информировавние, если нет данных о вызове в файле либо базе данных !!
        try:
            cus_data = json.loads(cus_data.replace("'", '"'))
            contract, dolg = cus_data[4], cus_data[3]
            ''' Тут надо добавить путь до файла с номером контракта и суммой долга: например autodial/172351'''
            pcon1 = await list_sound.check_contract(phone, contract)
            pcon3 = await list_sound.check_dolg(phone, dolg)
            urliz[1] += str(pcon1)
            urliz[3] += str(pcon3)
            '''if not contract or not dolg:
                # print(f"jobe_type::contract: {contract} dolg: {dolg}")
                logger.info(f"jobe_type::contract: {contract} dolg: {dolg}")
                return None
            else:
                # print(f"jobe_type::contract: {contract} dolg: {dolg}")
                logger.info(f"jobe_type::contract: {contract} dolg: {dolg}")'''
            # print(f"urliz: {urliz}")
        except JSONDecodeError as e:
            # print(f"JSONDecodeError: {e}")
            logger.exception(f"JSONDecodeError: {e}")
            return 'None', 'None'
        except Exception as e:
            logger.exception(f"NoneType: {e}")
            return 'None', 'None'
        return urliz
    elif jobe_type in "fizliz":
        fizliz, cus_data = await list_sound.individuals(ev)
        # print(f"customer_data: {cus_data}")
        logger.info(f"customer_data: {cus_data}")
        # TODO Сделать информировавние, если нет данных о вызове в файле либо базе данных !!
        try:
            cus_data = json.loads(cus_data.replace("'", '"'))
            contract, dolg = cus_data[4], cus_data[3]
            ''' Тут надо добавить путь до файла с номером контракта и суммой долга: например autodial/172351'''
            pcon1 = await list_sound.check_contract(phone, contract)
            pcon3 = await list_sound.check_dolg(phone, dolg)
            fizliz[1] += str(pcon1)
            fizliz[3] += str(pcon3)
            # print(f"fizliz: {fizliz}")
        except JSONDecodeError as e:
            # print(f"JSONDecodeError: {e}")
            logger.exception(f"JSONDecodeError: {e}")
            return 'None', 'None'
        return fizliz
    elif jobe_type in "fizlizcourt":
        fizlizcourt, cus_data = list_sound.individuals_with_court(ev)
        try:
            cus_data = json.loads(cus_data.replace("'", '"'))
            contract, dolg = cus_data[4], cus_data[3]
            # TODO проверить эти переменные!
            ''' Тут надо добавить путь до файла с номером контракта и суммой долга'''
            pcon1 = await list_sound.check_contract(phone, contract)
            pcon3 = await list_sound.check_dolg(phone, dolg)
            fizlizcourt[1] += str(pcon1)
            fizlizcourt[3] += str(pcon3)
            # print(f"fizlizcourt: {fizlizcourt}")
            logger.info(f"fizlizcourt: {fizlizcourt}")
        except JSONDecodeError as e:
            # print(f"JSONDecodeError: {e}")
            logger.exception(f"JSONDecodeError: {e}")
            return 'None', 'None'
        return fizlizcourt
    elif jobe_type in "summer":
        summer, cus_data = await list_sound.summer_water_supply(ev)
        try:
            cus_data = json.loads(cus_data.replace("'", '"'))
            contract, dolg = cus_data[4], cus_data[3]
            # TODO проверить эти переменные!
            ''' Тут надо добавить путь до файла с номером контракта и суммой долга'''
            # summer[1] += str(list_sound.check_contract(phone))
            pcon3 = await list_sound.check_dolg(phone, dolg)
            summer[1] += str(pcon3)
            # print(f"summer: {summer}")
        except JSONDecodeError as e:
            # print(f"JSONDecodeError: {e}")
            logger.exception(f"JSONDecodeError: {e}")
            return 'None', 'None'
        return summer
    elif jobe_type in "handstart":
        handstart = list_sound.handover_start_month()
        # print(f"handstart: {handstart}")
        logger.info(f"handstart: {handstart}")
    elif jobe_type in "handend":
        handend = list_sound.handover_end_month()
        # print(f"handend: {handend}")
        logger.info(f"handend: {handend}")


''' Обслуживание получаемых из Астериска данных.
    Постановка задачи для их реализации'''
class ARIInterface:
    """ Класс для обработки состояний вызова.
    Команды применяются для канала с идентификатором, получаемый от Астериска """

    # noinspection PyArgumentList
    def __init__(self, server_addr, username, password, env_):
        self._req_base = f"http://{server_addr}:8088/ari/"
        self._username = username
        self._password = password
        self.env = env_
        self.ws_push = Settings(_env_file=self.env, _env_file_encoding='utf-8').WS_PUSH
        self.datafile = Settings(_env_file=self.env, _env_file_encoding='utf-8').DATAFILE

    async def on_dial(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        # print(f"В канал {channel_id} идет вызов!\n")
        logger.info(f"В канал {channel_id} идет вызов!\n")
        ws_data = {"Dial in channel: ": channel_id}
        try:
            await curl_request(self.ws_push, ws_data, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def on_channel_state_change(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        # print(f"Статус канала {channel_id} изменился на {ev['channel']['state']}!\n")
        logger.info(f"Статус канала {channel_id} изменился на {ev['channel']['state']}!\n")
        ws_data = {"Dial in channel: ": channel_id}
        try:
            await curl_request(self.ws_push, ws_data, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def on_channel_varset(self, channel_id, ev, data):
        """

        :param data:
        :param channel_id:
        :param ev:
        """
        print(
            f"Тип автообзвона в канале {channel_id} - {ev['channel']['dialplan']['app_data'].rsplit(',', 1)[1]}"
            f"\nСо страницы прилетело: {data}"
        )
        try:
            await curl_request(self.ws_push, channel_id, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def on_stasis_start(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        # print("ARI Session started\n")
        logger.info("ARI Session started\n")
        await self.answer_call(channel_id, ev)
        ws_data = {"Start session channel: ": channel_id}
        try:
            await curl_request(self.ws_push, ws_data, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def on_playback_started(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        # print(f"\nPlayback в канал {channel_id} запуще! ")
        logger.info(f"Playback в канал {channel_id} запуще! ")
        ws_data = {"Playback в канал: ": channel_id}
        try:
            await curl_request(self.ws_push, ws_data, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def play_sound_in_auto_call(self, channel_id: object, param: object, ev: object) -> object:
        """
        
        :param channel_id:  # Это идентификатор канала
        :param param:       # Это зарезервированный параметр, он не используется
        :param ev:          # Это параметры канала
        :return:
        """
        phone = ev['channel']['connected']['number']
        # phone = '100'
        # print(f"\nev['channel']: {ev['channel']}\n")  # import sys; sys.exit()
        # print(f"ws_data: {phone} : {param} : {ev}")-
        '''
        """ Получаем путь до файла csv со списком параметров клиентов """
        pwd_path = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 2)[0]
        # print(add_path)
        # os.chdir(add_path)
        path_to_config_file = pwd_path + os.sep + self.datafile'''

        """ Получаем список адресов голосовых файлов из функции checking_job_type """
        job_type = await checking_job_type(phone, FILENAME, ev, self.ws_push, self.env)
        # print(f"play_sound_in_auto_call::job_type: {job_type}")
        logger.info(f"play_sound_in_auto_call::job_type: {job_type}")

        playback_id = str(uuid.uuid4())
        plays = ','.join(list(map('sound:'.__add__, job_type)))
        req_str = self._req_base + f"channels/{channel_id}/play/{playback_id}?media={plays}&lang=ru"
        await self._send_post_request(req_str)

    async def on_playback_finished(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        # print(f"Воспроизведение {channel_id} завершено")
        logger.info(f"Воспроизведение {channel_id} завершено")
        """По окончанию проигрывания - ложим трубку."""
        # print(f"\nPlayback в канал {list(channel_id.values())[2]['target_uri'].split(':')[1]} окончен, HangUp ")
        # print(f"\nPlayback в канал {channel_id} окончен, HangUp!")
        logger.info(f"Playback в канал {channel_id} окончен, HangUp!")
        await self.hangup_call(channel_id, ev)
        # channel_ = self.get("channel")
        # channel_obj.get("channel")
        try:
            await curl_request(self.ws_push, channel_id, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def answer_call(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        req_str = self._req_base + f"channels/{channel_id}/answer"
        req = await self._send_post_request(req_str)
        ws_data = {"Answer channel: ": req}
        try:
            await curl_request(self.ws_push, ws_data, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def on_stasis_end(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        # print(f"Stasis Session {channel_id} ended\n")
        logger.info(f"Stasis Session {channel_id} ended\n")
        await self.hangup_call(channel_id, ev)

    async def on_channel_hangup_request(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        # print(f"Получен запрос на отключение канала {channel_id}!")
        logger.info(f"Получен запрос на отключение канала {channel_id}!")
        await self.hangup_call(channel_id, ev)

    async def hangup_call(self, channel_id, ev):
        """

        :param channel_id:
        :param ev:
        """
        req_str = self._req_base + f"channels/{channel_id}?reason_code=16"
        # curl -X DELETE req_str = self._req_base + f"channels/1611210929.1075?reason_code=16&api_key" -H  "accept: */*"
        # req_str = self._req_base + f"channels/1611210929.1075?reason_code=16&api_key"
        await self._send_delete_request(req_str)
        ws_data = {"HandUp in channel: ": channel_id}
        try:
            await curl_request(self.ws_push, ws_data, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def on_channel_other(self, ev):
        """

        :param ev:
        """
        ws_data = {"Start session channel: ": ev}
        try:
            await curl_request(self.ws_push, ws_data, ev)
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')

    async def _send_post_request(self, req_str):
        r = await requests.post(req_str, auth=(self._username, self._password))
        '''
        try:
            await curl_request(self.ws_push, req_str, )
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')
        '''
        return r.text

    async def _send_delete_request(self, req_str):
        r = await requests.delete(req_str, auth=(self._username, self._password))
        '''
        try:
            await curl_request(self.ws_push, req_str, )
        except IOError as er:
            # print(f'IOError||: {er}')
            logger.exception(f'IOError||: {er}')
        '''
        # print(r.status_code)
        return r.status_code
        # print(r.text())

    '''
    do_hang = False

    async def music_on_hold(self, channel_id, moh_class):
        # print("in music_on_hold()")
        logger.info("in music_on_hold()")
        # print(self._req_base + f"channels/{channel_id}/moh?mohClass=custom")
        logger.info(self._req_base + f"channels/{channel_id}/moh?mohClass=custom")
        req_str = self._req_base + f"channels/{channel_id}/moh?mohClass={moh_class}"
        await self._send_post_request(req_str)
    async def music_unhold(self, channel_id):
        # print("unhold the music")
        logger.info("unhold the music")
        # stopMoh
        # print(self._req_base + f"channels/{channel_id}/moh")
        logger.info(self._req_base + f"channels/{channel_id}/moh")
        req_str = self._req_base + f"channels/{channel_id}/moh"
        await self._send_delete_request(req_str)
    async def on_channel_dtmf_received(self, channel_id, digit):
        self.do_hang = True
        # print("DTMF Received: " + digit)
        logger.info("DTMF Received: " + digit)
        # on any dtmf stop the stasis Application and goto next prirorty.
        # self.continue_in_dialplan(channel_id, ev)
        if '1' == digit:
            await self.music_on_hold(channel_id, 'custom')

        elif '2' == digit:
            await self.music_unhold(channel_id)

        if '3' == digit:
            await self.music_on_hold(channel_id, 'default')

        elif '4' == digit:
            await self.music_unhold(channel_id)'''
    '''async def play_sound(self, channel_id, sound_name):
        """

        :param channel_id:
        :param sound_name:
        :return:
        """
        playback_id = str(uuid.uuid4())
        req_str = self._req_base + f"channels/{channel_id}/play/{playback_id}?media=sound:{sound_name}&lang=ru"
        # req_str = self._req_base + (f"channels/{channel_id}/play/{playback_id}?media=sound:{sound_name}&lang=ru")
        await self._send_post_request(req_str)'''


''' Создание подключения к Астериску.
    Создание приложения в Астериске типа Stasis.
    Получение данных из Астериска
    Формирование задач по обслуживанию вызова, поступившего в приложение'''


class ARIApp(object):
    """ Класс для создания канала обмена данными с Астериском, типа websocket.
    В зависимости от получаемых данных выполяются определенные команды,
    посылаемые в RESTfull API Астериск """

    run_file = '/var/run/user/1000'

    # noinspection PyArgumentList
    def __init__(self, env_):
        """
        Инициализация переменных для создания подключения

        :param env_:
        """
        # print(f'env: {env_}')  #; import sys; sys.exit()
        # logger.info(f'env: {env_}')  # ; import sys; sys.exit()
        self.env = env_
        self.pathf = Settings(_env_file=env_, _env_file_encoding='utf-8').PATHF
        self.app_name = Settings(_env_file=self.env, _env_file_encoding='utf-8').STSPPS
        self.username = Settings(_env_file=self.env, _env_file_encoding='utf-8').ARIUSER
        self.password = Settings(_env_file=self.env, _env_file_encoding='utf-8').PASSW
        self.server_addr = Settings(_env_file=self.env, _env_file_encoding='utf-8').SADDR
        # 'c94be586c3e2cfe9023b9c663ed6c526'
        self.url = f"ws://{self.server_addr}:8088/ari/events?app={self.app_name}" \
                   f"&api_key={self.username}:{self.password}"
        self.ari = ARIInterface(self.server_addr, self.username, self.password, self.env)
        self.pid = os.getpid()
        self.ppid = os.getppid()
        # print(f"self.url: {self.url}")
        logger.info(f"self.url: {self.url}")
        # print(f"self.pid: {self.pid}")
        logger.info(f"self.pid: {self.pid}")
        # print(f"self.ppid: {self.ppid}")
        logger.info(f"self.ppid: {self.ppid}")
        # print(f"run_file = '/var/run/user/1000/asuncio_autodial.pid'")
        #logger.info(f"run_file = '/var/run/user/1000/asuncio_autodial.pid'")


    async def connect(self, data):
        """

        :rtype: object
        """
        logger.info(f"data: {data}")
        async with websockets.connect(self.url) as websocket:
            """ Создание подключения к Астериску """
            # print(f"Connected..{data}")            # print(f"self.pathf: {str(self.pathf)}")
            logger.info(f"Connected..{data}")  # print(f"self.pathf: {str(self.pathf)}")

            while True:
                """ Ожидание данных из сокета: await websocket.recv() """
                event_str = await websocket.recv()
                event_json = json.loads(event_str)

                if event_json['type'] == 'Dial':
                    channel_id = event_json['peer']['id']
                    await self.ari.on_dial(channel_id, event_json)

                elif event_json['type'] == 'ChannelStateChange':
                    channel_id = event_json['channel']['id']
                    await self.ari.on_channel_state_change(channel_id, event_json)

                elif event_json['type'] == 'ChannelVarset':
                    # if event_json["variable"] == "STASISSTATUS":
                    channel_id = event_json['channel']['id']
                    await self.ari.on_channel_varset(channel_id, event_json, data)

                elif event_json['type'] == 'StasisStart':
                    """ Если статус канала StasisStart - принимаем вызов и воспроизводим музыку """
                    await self.ari.answer_call(event_json['channel']['id'], event_json)
                    channel_id = event_json['channel']['id']
                    await self.ari.play_sound_in_auto_call(channel_id, 'tt-monkeys', event_json)

                elif event_json['type'] == 'PlaybackStarted':
                    channel_id = event_json['playback']['target_uri'].split(':')[1]
                    # print(f"\nPlayback в канал {channel_id} запуще! ")
                    logger.info(f"Playback в канал {channel_id} запуще! ")
                    await self.ari.on_playback_started(channel_id, event_json)

                elif event_json['type'] == 'PlaybackFinished':
                    channel_id = event_json['playback']['target_uri'].split(':')[1]
                    await self.ari.on_playback_finished(channel_id, event_json)

                elif event_json['type'] == 'ChannelHangupRequest':
                    channel_id = event_json['channel']['id']
                    await self.ari.on_channel_hangup_request(channel_id, event_json)

                elif event_json['type'] == 'StasisEnd':
                    channel_id = event_json['channel']['id']
                    await self.ari.on_stasis_end(channel_id, event_json)

                elif event_json['type'] in 'ChannelDestroyed' or 'ChannelUnhold':
                    await self.ari.on_channel_other(event_json)

                else:
                    # print(f"\n\nWebsocket event***************************************************\n{event_json}\n")
                    logger.info(
                        f"\n\nWebsocket event***************************************************\n{event_json}\n")


async def main_start(_env):
    """

    :param _env:
    """
    logger.info(f"main_start::_env: {_env}")
    await ARIApp(_env).connect(typeauto)


typeauto = 'fizliz'


async def main(_env, _typeauto, test=None):
    """

    :param _env:        # Это путь до файла с конфигурацией
    :param _typeauto:   # Это планировалось как тип автообзвона
    :param test:        # Это просто затычка для работы инструкций ниже if __name__ == '__main__':
    """
    logger.info(f"__name__:::main::_env: {_env}")
    await main_start(_env)


if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(main_start)
    # asyncio.run(main(env))
    with suppress(KeyboardInterrupt):  #
        # logger.info(f"__name__:::main_start::env: {env}")
        uvicorn.run(
            "autodial_apps:main", host="0.0.0.0", port=8765,
            reload=True, log_level="debug", debug=True, lifespan='on'
        )

'''
        try:
            print("running")
            asyncio.get_event_loop().run_forever()
        except KeyboardInterrupt:
            print("server crashed")
'''
