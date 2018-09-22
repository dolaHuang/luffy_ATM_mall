#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 9:04
# @Author  : DolA
# @Site    : 
# @File    : setting.py
# @Software: PyCharm
import os
import logging
# 本程序最外层路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 账户数据文件的路径
DB_path = '%s\\db\\accounts' % BASE_DIR
# 日志文件路径
LOG_path = '%s\\logs' % BASE_DIR
# 日志级别
LOG_LEVEL = logging.INFO
# 日志类型
LOG_TYPES = {
    'access': 'access.log',
    'transactions': 'transactions.log',
    'admin': 'admin_management.log'
}
# 账户操作类型
TRANSACTION_TYPE = {
    'pay_back': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'transfer_rec': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0},
}

# 账户格式
account_dic = {
    'id': '',
    'password': '',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '',
    'expire_date': '',
    'pay_day': '',
    'status': 0  # 0 = normal, 1 = locked, 2 = disabled
}
