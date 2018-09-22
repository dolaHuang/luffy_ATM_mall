#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 13:12
# @Author  : DolA
# @Site    : 
# @File    : decorator_mall.py
# @Software: PyCharm
import os
from atm.conf import setting
from atm.core import auth
from atm.core import logger
from atm.core import message_utils
flag = False

user_obj = {  # 存储登陆账户的状态和数据
        'authenticated': False,
        'user_data': None
    }


# 装饰器登陆认证
def login(func, *args, **kwargs):
    """

    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    def inner(*args, **kwargs):
        global flag, user_obj
        if user_obj['authenticated']:
            return func(user_obj, *args)
        else:
            while not user_obj['authenticated']:
                account = input('\033[1;34;0m enter your ATM ID>>\033[0m')
                password = input('\033[1;34;0m enter your Password>>\033[0m')
                user_data = auth.atm_authenticated(account, password)
                if user_data:
                    flag = True
                    user_obj['authenticated'] = True
                    user_obj['user_data'] = user_data
                    msg = 'user %s just logged in' % user_obj['user_data']['id']
                    log_file = os.path.join(setting.LOG_path, setting.LOG_TYPES['access'])
                    logger.logger(log_file, msg)
                    return func(user_obj, *args)
                else:
                    msg1 = 'Account number or password error'
                    message_utils.print_error(msg1)
    return inner

