#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 9:04
# @Author  : DolA
# @Site    : 
# @File    : manage.py
# @Software: PyCharm
import os
from atm.core import logger
from atm.core import admin_func
from atm.core import decorator
from atm.conf import setting
from atm.core import message_utils

admin_func = [
        ('add account', admin_func.add_account),
        ('adjust credit', admin_func.adjust_credit),
        ('frozen account', admin_func.frozen_account)
    ]


# 管理接口
@decorator.login
def manage(user_obj, *args):
    # 判断 输入是不是管理员账号
        if user_obj['user_data']['id'] == 'admin' and user_obj['user_data']['password'] == 'admin':
            # 日志
            log_file = os.path.join(setting.LOG_path, setting.LOG_TYPES['admin'])
            msg = 'admin login'
            logger.logger(log_file, msg)
            # 打印功能 供用户选择
            while True:
                print('\033[1;30;0m')  # 高亮
                print('admin'.center(30, '-'))
                for i, v in enumerate(admin_func):
                    print(i, '>', v[0])
                print('\033[0m')  # 高亮
                choice = input('\033[1;34;0m enter your choice/q>>\033[0m').strip()
                if choice.isdigit():
                    choice = int(choice)
                    if 0 <= choice <= len(admin_func):
                        admin_func[choice][1](user_obj['user_data']['id'])
                    else:
                        msg = 'Wrong number'
                        message_utils.print_error(msg)
                elif choice == 'q':
                    msg = 'Exit admin interface'
                    message_utils.print_enter(msg)
                    break
                elif choice == 'exit':
                    exit('bye')
                else:
                    msg = 'Wrong number'
                    message_utils.print_error(msg)


