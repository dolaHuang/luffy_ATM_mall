#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 9:06
# @Author  : DolA
# @Site    : 
# @File    : main.py
# @Software: PyCharm
import os
from atm.conf import setting
from atm.core import logger
from atm.core import logics
from atm.core import decorator
from atm.core import message_utils
features = [
    ('account_info', logics.view_account_info),
    ('withdraw', logics.withdraw),
    ('pay_back', logics.pay_back),
    ('transfer', logics.transfer),
    ('admin', logics.admin)
]


# 功能分发
@decorator.login
def func_controller(user_obj):
    """
    推出 也要记录日志
    :param user_obj:
    :return:
    """
    while True:
        print('\033[1;30;0m')
        print('------ Welcome to ATM ------')
        for index, val in enumerate(features):
            print(index, '>', val[0])
        print('\033[0m')
        choice = input('\033[1;34;0m enter your choice/q>>\033[0m').strip()
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(features):
                features[choice][1](user_obj['user_data'])
            else:
                msg1 = 'Wrong number'
                message_utils.print_error(msg1)
        elif choice == 'q':
            msg = 'user %s Logged out' % user_obj['user_data']['id']
            log_file = os.path.join(setting.LOG_path, setting.LOG_TYPES['access'])
            logger.logger(log_file, msg)
            msg2 = 'Exit ATM'
            message_utils.print_error(msg2)
            break
        else:
            msg3 = 'error enter!'
            message_utils.print_error(msg3)

