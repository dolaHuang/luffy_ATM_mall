#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 8:30
# @Author  : DolA
# @Site    : 
# @File    : decorator_mall.py
# @Software: PyCharm
from shopping_mall.core import auth_mall
from atm.core import logger
from shopping_mall.conf import setting_mall
import os
from atm.core import message_utils
user_obj = {  # 存储登陆账户的状态和数据
        'authenticated': False,
        'user_data': None
    }


# 商城登陆装饰器
def login_mall(func, *args):
    """
    {"account": {"username": "alex", "password":"1234"}, "shopping_cart": {"电脑": {"number": 2, "price": 3998},
    "美女": {"number": 2, "price": 1996}, "游艇": {"number": 5, "price": 100}}}
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        global user_obj
        if user_obj['authenticated']:
            return func(user_obj, *args)
        else:
            while not user_obj['authenticated']:
                username = input('\033[1;34;0menter your username>>\033[0m')
                password = input('\033[1;34;0menter your password>>\033[0m')
                user_data = auth_mall.auth_mall_authenticated(username, password)
                if user_data:
                    user_obj['authenticated'] = True
                    user_obj['user_data'] = user_data
                    # 日志
                    msg = 'user %s just logged in mall' % user_obj['user_data']['account']['username']
                    log_file = os.path.join(setting_mall.LOG_PATH, setting_mall.LOG_TYPES['access'])
                    logger.logger(log_file, msg)
                    return func(user_obj, *args)
                else:
                    msg1 = 'Account number or password error'
                    message_utils.print_error(msg1)
    return inner
