#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 8:33
# @Author  : DolA
# @Site    : 
# @File    : setting_mall.py
# @Software: PyCharm
import os
from shopping_mall.core import main

BASE_DIR_MALL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 商城日志路径
LOG_PATH = '%s\\logs' % BASE_DIR_MALL
# 商城账户 路径
ACCOUNT_MALL_PATH = '%s\\db\\account' % BASE_DIR_MALL
# 商品列表
GOODS_LIST = [
    {"name": "Computer", "price": 1999},
    {"name": "mouse", "price": 10},
    {"name": "houseboat", "price": 20},
    {"name": "Sexy belle", "price": 998},
]
# 商城功能
mall_home = [
    ('Shopping', main.shopping_mall),
    ('View shopping cart', main.shopping_mall_cart)
    ]
# 商城 日志类型
LOG_TYPES = {
    'access': 'access_mall.log',
    'transactions': 'transactions_mall.log'
}
