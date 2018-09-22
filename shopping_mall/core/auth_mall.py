#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 8:49
# @Author  : DolA
# @Site    : 
# @File    : auth_mall.py
# @Software: PyCharm
from shopping_mall.conf import setting_mall
from atm.core import db_handler
import os


# 认证账号
def auth_mall_authenticated(username, password):
    """
    {"account": {"username": "alex", "password":"1234"}, "shopping_cart": {"电脑": {"number": 2, "price": 3998},
    "美女": {"number": 2, "price": 1996}, "游艇": {"number": 5, "price": 100}}}
    :return:
    """
    account_mall_file = os.path.join(setting_mall.ACCOUNT_MALL_PATH, '%s.json' % username)
    username_data = db_handler.load_account_data(account_mall_file)
    if username_data:
        if username_data['account']['username'] == username and username_data['account']['password'] == password:
            return username_data
