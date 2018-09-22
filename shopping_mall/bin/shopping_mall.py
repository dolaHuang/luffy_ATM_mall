#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 12:21
# @Author  : DolA
# @Site    : 
# @File    : shopping_mall.py
# @Software: PyCharm
import os
from shopping_mall.conf import setting_mall
from atm.core import logger
from shopping_mall.core import decorator_mall
from atm.core import message_utils


# 运行购物商城
@decorator_mall.login_mall
def run_mall(user):
    while True:
        print('\033[1;30;0m')
        print('------Welcome to shopping_mall------')
        for i, v in enumerate(setting_mall.mall_home):
            print(i, '>>', v[0])
        print('\033[1;30;0m')
        choice = input('\033[1;34;0mPlease enter your choice/q>>\033[0m').strip()
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice <= len(setting_mall.mall_home):
                setting_mall.mall_home[choice][1](user)
            else:
                msg1 = 'Wrong number'
                message_utils.print_error(msg1)
        elif choice == 'q':
            msg2 = 'Exit shopping mall'
            message_utils.print_info(msg2)
            # 日志
            msg = 'user %s just logged out mall' % user['user_data']['account']['username']
            log_file = os.path.join(setting_mall.LOG_PATH, setting_mall.LOG_TYPES['access'])
            logger.logger(log_file, msg)
            break
        else:
            msg3 = 'error enter!'
            message_utils.print_error(msg3)


