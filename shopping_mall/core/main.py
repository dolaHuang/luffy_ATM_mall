#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 12:21
# @Author  : DolA
# @Site    :
# @File    : main.py
# @Software: PyCharm
import os
from atm.core import logger
from atm.core import db_handler
from shopping_mall.core import check_out_mall
from tabulate import tabulate
from shopping_mall.core import decorator_mall
from shopping_mall.conf import setting_mall
from atm.core import message_utils


# 购物车
@decorator_mall.login_mall
def shopping_mall_cart(user, *args):
    """
    {"account": {"username": "alex", "password":"1234"}, "shopping_cart": {"电脑": {"number": 2, "price": 3998},
    "美女": {"number": 2, "price": 1996}, "游艇": {"number": 5, "price": 100}}}
    :param user:
    :return:
    """
    account = user['user_data']['account']['username']  # 帐户名
    # 进入函数，先记日志
    msg = 'user %s view shopping cart' % account
    file = os.path.join(setting_mall.LOG_PATH, setting_mall.LOG_TYPES['access'])
    logger.logger(file, msg)

    shopping_list = []   # 用于打印购物车列表
    user_data_cart = user['user_data']['shopping_cart']
    if user_data_cart:
        cash_total = 0
        print('\033[1;30;0m')
        print('goods list'.center(40, '*'))
        for key, value in user_data_cart.items():
            shopping_list.append([key, value['number'], value['price'] / value['number'], value['price']])
            cash_total += value['price']
        print(tabulate(shopping_list, headers=('商品', '数量', '单价', '总价'), tablefmt='grid'))
        print('total of consumption:%s' % cash_total)
        print('END'.center(40, '*'))
        print('\033[0m')
        # 选择 是否结账
        while True:
            print("""\033[1;30;0m
         1. Check out by ATM
         2. Return to the mall
                         \033[0m""")
            choice = input('\033[1;34;0m enter your choice>>\033[0m').strip()
            if choice == '1':
                result = check_out_mall.check_out(user, cash_total, *args)
                if result:
                    break
            elif choice == '2':
                break
            else:
                msg1 = 'Error enter!'
                message_utils.print_error(msg1)
    else:
        print('Dear\033[1;31;0m%s\033[0m\n you have no goods in cart!' % account)


# 购物，选择商品
@decorator_mall.login_mall
def shopping_mall(user, *args):
    account = user['user_data']['account']['username']  # 账号名
    while True:
        print('\033[1;30;0m')
        print('Shopping Mall'.center(36, '-'))
        for i, k in enumerate(setting_mall.GOODS_LIST):   # 循环购物车，选择商品
            print(i, k['name'], k['price'])
        print('\033[0m')
        choice = input('\033[1;34;0mEnter your choice /q >>\033[0m')
        shopping_cart = user['user_data']['shopping_cart']   # 这是用户购物车
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice <= len(setting_mall.GOODS_LIST):
                goods_name = setting_mall.GOODS_LIST[choice]['name']  # 这是用户选择的商品
                if shopping_cart.get(goods_name) is None:
                    shopping_cart[goods_name] = {'number': 1, 'price': setting_mall.GOODS_LIST[choice]['price']}

                else:
                    shopping_cart[goods_name]['number'] += 1
                    shopping_cart[goods_name]['price'] += setting_mall.GOODS_LIST[choice]['price']
                # 记日志
                msg = 'user %s add a %s to shopping cart' % (account, goods_name)
                file = os.path.join(setting_mall.LOG_PATH, setting_mall.LOG_TYPES['access'])
                logger.logger(file, msg)
                # 序列化
                file_mall = os.path.join(setting_mall.ACCOUNT_MALL_PATH, '%s.json' % account)
                db_handler.json_data(user['user_data'], file_mall, status=1)
            else:
                print('\033[1;31;0m\033[0mWrong number！\033[0m')
        elif choice == 'q':
            if shopping_cart:
                # 调用函数，将购物车的商品信息提取出来，打印成表格显示
                shopping_mall_cart(user)
                break
            else:
                print('Dear\033[1;31;0m%s\033[0m\n you have no goods in cart!' % account)
                break
        else:
            print('\033[1;31;0mWrong number！\033[0m')
