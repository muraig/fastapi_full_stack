#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

from __future__ import print_function

import os
import time
import uuid
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import json

# from config import Settings
#os.chdir(os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0])
#print(os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0] + os.sep + 'office.env')
add_path = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0]
os.chdir(add_path)
print(f"add_path: {add_path}")
'''
'''
print(f"env: {os.listdir()}");
import pkgutil
search_path = ['..'] # Используйте None, чтобы увидеть все модули, импортируемые из sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)
#import sys ; sys.exit()
try:
    from config.config import Settings
except:
    from config import Settings
#import sys; sys.exit()

'''env_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 3)[0] + os.sep
print(os.path.abspath(os.path.dirname(__file__)).rsplit('/', 3)[0] + os.sep)
# env = env_root + 'office.env'
env = env_root + '.env'
'''
env_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 2)[0] + os.sep
env = env_root + '.env'
# print(f"env: {env}")

config = Settings(_env_file=env,
                  _env_file_encoding='utf-8')

# Configure API key authorization: app_id
configuration = swagger_client.Configuration()
# configuration.host = 'http://192.168.7.249:8088/ari'
# configuration.api_key['api_key'] = 'pbxuser:e07026d612c56a4ec8f62273ed366e48'
configuration.host = config.URLARI
configuration.api_key['api_key'] = config.API_KEY


def create_channels_with_id(_phone, _channel_id):
    api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
    endpoint = 'PJSIP/' + str(_phone)
    channel_id = _channel_id
    #  { "endpoint": "SIP/Alice", "variables": { "CALLERID(name)": "Alice" } } (optional)
    body = swagger_client.Containers()
    # extension = 'extension_example'
    # context = 'context_example'
    # priority = 789
    label = 'label_example'
    # app = 'channel-playback-monkeys'
    # app = 'channel-tones'
    # app = 'hello'
    app = 'channel-playback'
    app_args = 'externalCall,summer'
    app_args = 'externalCall,urliz'
    app_args = 'externalCall,fizlizcourt'
    app_args = 'externalCall,fizliz'
    caller_id = _phone
    timeout = 60
    # //other_channel_id = 'other_channel_id_example'
    # //originator = 'originator_example'
    # formats = 'formats_example'

    api_response = None

    try:
        #  Create a new channel (originate with id).
        # please pass async_req=True
        # thread = api.originate_with_id(endpoint, channel_id, async_req=True)
        # result = thread.get()
        api_response = api_instance.originate_with_id(endpoint, channel_id, body=body, _return_http_data_only=True,
                                                      # extension=extension, context=context, priority=priority,
                                                      label=label, app=app, app_args=app_args,
                                                      caller_id=caller_id, timeout=timeout, async_req=True)
        result = api_response.get()
        # , other_channel_id=other_channel_id, originator=originator)
        # ,formats=formats)
        # pprint(api_response)
        #print(result)
        #pprint(result)
    except ApiException as e:
        pprint("Exception when calling ChannelsApi->originate_with_id: %s\n" % e)
    if result:
        data = api_instance.getchannel(_channel_id, async_req=False)
        print(f'\napi_instance.getchannel(_channel_id):'
              f'{data.state}\n'
              )
        # data = data.replace(',\n', ',')
    '''
    '''
    return result


class Test(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


if __name__ == '__main__':
    phone = config.PHONE1
    _time = str(time.time())
    _uniq = str(uuid.uuid4())
    ch_id = _time + '-' + _uniq

    res = create_channels_with_id(phone, ch_id)
    print(f"create_channels_with_id:\n{res}")
    #print(f"create_channels_with_id: {res.get()}")
    print(f"create_channels_with_id: {type(res)}")
    #print(f"create_channels_with_id:\n{res.__repr__}")

'''
    def __init__(self, accountcode=None, caller=None, channelvars=None, connected=None, creationtime=None, dialplan=None, id=None, language=None, name=None, state=None):  # noqa: E501
    def accountcode(self):
    def accountcode(self, accountcode):
    def caller(self):
    def caller(self, caller):
    def channelvars(self):
    def channelvars(self, channelvars):
    def connected(self):
    def connected(self, connected):
    def creationtime(self):
    def creationtime(self, creationtime):
    def dialplan(self):
    def dialplan(self, dialplan):
    def id(self):
    def id(self, id):
    def language(self):
    def language(self, language):
    def name(self):
    def name(self, name):
    def state(self):
    def state(self, state):
    def to_dict(self):
    def to_str(self):
    def __repr__(self):
    def __eq__(self, other):
    def __ne__(self, other):
'''
'''
ORIGINATE_STATUS - This indicates the result of the call origination.
    FAILED
    SUCCESS
    BUSY
    CONGESTION
    HANGUP
    RINGING
    UNKNOWN - In practice, you should never see this value. Please report it to the issue tracker if you ever see it.
'''
