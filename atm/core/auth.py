#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 9:06
# @Author  : DolA
# @Site    : 
# @File    : auth.py
# @Software: PyCharm
import os
import time
from atm.conf import setting
from atm.core import db_handler
from atm.core import message_utils


# 用户账户认证
def atm_authenticated(account_number, password):
    """
     1、对比成功，就返回数据
    :param account_number:
    :param password:
    :return:
    """
# 反序列化
    account_file = os.path.join(setting.DB_path, '%s.json' % account_number)
    account_data = db_handler.load_account_data(account_file)
    if account_data:
        if account_data['password'] == password:
            if account_data['status'] == 0:
                time_now = time.time()
                time_expire = time.mktime(time.strptime(account_data['expire_date'], format('%Y-%m-%d')))
                if time_expire - time_now > 0:
                    return account_data
                else:
                    msg = 'The account over time'
                    message_utils.print_error(msg)
                    return None
            elif account_data['status'] == -1:
                msg2 = 'The account has been frozen!'
                message_utils.print_error(msg2)
                return None
        else:
            return None



