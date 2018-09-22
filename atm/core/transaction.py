#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 9:07
# @Author  : DolA
# @Site    : 
# @File    : transaction.py
# @Software: PyCharm
import os
from atm.conf import setting
from atm.core import db_handler
from atm.core import logger
from atm.core import message_utils


# 账户交易的具体操作，如对账户余额的计算
def make_transaction(user_data, tran_type, cash):
    """
    1.确定tran_type 在setting设定的 类型中
    2.根据设定的类型对数据进行操作
    3.把数据跟新到文件
    4.写日志
    :param user_data:
    :param tran_type:
    :param cash:
    :return:
    """
    new_balance = 0
    if tran_type in setting.TRANSACTION_TYPE:
        interest = cash * setting.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = user_data['balance']
        if setting.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + cash + interest
        elif setting.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - cash - interest
        if new_balance > 0:
            user_data['balance'] = new_balance
            # 序列化
            file = os.path.join(setting.DB_path, '%s.json' % (user_data['id']))
            user_data = db_handler.json_data(user_data, file, status=1)
            # 记日志
            msg = 'user %s %s cash: %s' % (user_data['id'], tran_type, cash)
            log_file = os.path.join(setting.LOG_path, setting.LOG_TYPES['transactions'])
            logger.logger(log_file, msg)
            return '%s succeeded!' % tran_type
        else:
            msg1 = 'There is not enough balance!'
            message_utils.print_error(msg1)
    else:
        print("\033[1;34;0mTransaction type [%s] is not exist!\033[0m" % tran_type)

