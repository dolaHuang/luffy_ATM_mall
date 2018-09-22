#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 19:45
# @Author  : DolA
# @Site    : 
# @File    : check_out_mall.py
# @Software: PyCharm
import os
from atm.core import logics
from atm.core import db_handler
from shopping_mall.conf import setting_mall
from atm.core import logger
from atm.core import message_utils


# 结算
def check_out(user, cash_total, *args):
    """
    1.如果返回True，表示 扣款成功
    2.清空购物车.序列化文件
    3.记日志
    :param user:
    :param cash_total:
    :param args:
    :return:
    """
    username = user['user_data']['account']['username']  # 商城账户名
    # 调用ATM 结算
    result = logics.mall_interface(user, cash_total, *args)
    if result:
        # 写日志
        msg = '%s cost %s pay for by ID:%s to buy something(%s)' % (username, cash_total, result[1], user['user_data']['shopping_cart'])
        file = os.path.join(setting_mall.LOG_PATH, setting_mall.LOG_TYPES['transactions'])
        logger.logger(file, msg)
        # 将清空购物车的 账户数据序列化
        user['user_data']['shopping_cart'] = {}
        file = os.path.join(setting_mall.ACCOUNT_MALL_PATH, '%s.json' % username)
        db_handler.json_data(user['user_data'], file, status=1)
        msg1 = 'Settlement of success!'
        message_utils.print_succeed(msg1)
        return result


