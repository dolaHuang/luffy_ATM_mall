#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 21:12
# @Author  : DolA
# @Site    : 
# @File    : logics.py
# @Software: PyCharm
import os
from atm.conf import setting
from atm.core import logger
from atm.core import transaction
from atm.core import db_handler
from atm.bin import manage
from atm.core import decorator
from atm.core import auth
from atm.core import message_utils


# 查看账户信息
@decorator.login
def view_account_info(user_obj, *args, **kwargs):
    """
    1打印信息
    2记录日志
    :param user_data:{'id': 888888, 'password': '1234', 'credit': 15000, 'balance': 15000, 'enroll_data': '2016-01-02',
    'expire_data': '2021-01-01', 'pay_day': 22, 'status': 0}
    :return:
    """
    print('\033[1;36;0m')
    print('Account Info'.center(30, '-'))
    for k, v in user_obj['user_data'].items():
        if not k == 'password':
            print('%12s:%s' % (k, v))
    print('END'.center(30, '-'))
    print('\033[0m')
    msg = 'user %s just View account information' % user_obj['user_data']['id']
    log_file = os.path.join(setting.LOG_path, setting.LOG_TYPES['access'])
    logger.logger(log_file, msg)


# 显示账户额度信息
@decorator.login
def balance_info(user_obj, *args):
    current_balance = """\033[1;36;0m-------- BALANCE INFO -------
    Credit :    %s
    Balance:    %s\033[0m
    """ % (user_obj['user_data']['credit'], user_obj['user_data']['balance'])
    print(current_balance)


# 取现
@decorator.login
def withdraw(user_obj, *args, **kwargs):
    """
    显示额度信息
    提示可取现金额
    判断是否可以提现，可能取现额度已经用完
    1.输入金额
    2.提示最大可取现金额
    3.对比，并提示
    4.调用transaction
    :param user_data:user_data:{'id': 888888, 'password': '1234', 'credit': 15000, 'balance': 15000, 'enroll_data': '2016-01-02',
    'expire_data': '2021-01-01', 'pay_day': 22, 'status': 0}
    :param args:
    :param kwargs:
    :return:
    """
    balance_info(user_obj['user_data'])
    withdraw_cash = round(user_obj['user_data']['balance']-user_obj['user_data']['credit']/2, 2)  # 可取现金额
    if withdraw_cash > 0:
        print('\033[1;36;0mThe amount you can cash out：\033[0m', withdraw_cash)
        cash = input('\033[1;34;0mPlease enter the cash of withdrawal >>\033[0m').strip()
        if cash.isdigit():
            if user_obj['user_data']['balance'] > withdraw_cash:
                cash = float(cash)
                if 0 <= cash <= withdraw_cash:
                    result_val = transaction.make_transaction(user_obj['user_data'], 'withdraw', cash)
                    if result_val:
                        print(result_val)
                else:
                    print('\033[1;36;0mThe amount you can cash out：\033[0m', withdraw_cash)
        else:
            msg = 'Please enter a correct number'
            message_utils.print_error(msg)
    else:
        msg2 = 'Unable to withdraw(The maximum withdrawal amount is half the amount！)'
        message_utils.print_error(msg2)


# 还款
@decorator.login
def pay_back(user_obj, *args, **kwargs):
    """
    1.显示额度信息
    2.显示需还款信息
    3.输入还款金额
    4.调用transaction

    :param user_data:{'id': 888888, 'password': '1234', 'credit': 15000, 'balance': 15000, 'enroll_data': '2016-01-02',
    'expire_data': '2021-01-01', 'pay_day': 22, 'status': 0}
    :param args:
    :param kwargs:
    :return:
    """
    balance_info(user_obj['user_data'])
    pay_back_cash = user_obj['user_data']['credit']-user_obj['user_data']['balance']
    print('\033[1;36;0mThe cash you need pay back：\033[0m', pay_back_cash)
    if pay_back_cash > 0:
        cash = input('\033[1;34;0mPlease input the amount you want to pay>>\033[0m').strip()
        if cash.isdigit():
            cash = float(cash)
            if 0 < cash:
                result_val = transaction.make_transaction(user_obj['user_data'], 'pay_back', cash)
                if result_val:
                    print(result_val)
            else:
                msg = 'Please enter a correct number!'
                message_utils.print_error(msg)
        else:
            msg1 = 'Please enter a correct number!'
            message_utils.print_error(msg1)
    else:
        msg2 = 'Unable to pay back!'
        message_utils.print_error(msg2)


# 转账
@decorator.login
def transfer(user_obj, *args, **kwargs):
    """
    1.显示额度信息 调用balance_info(user_data)
    2.判断账户余额 是否大于0 ，可能卡已经刷爆
    2.输入转入帐户 账号
    3.输入转出金额
    4。调用transaction
    :param user_data:
    :param args:
    :param kwargs:
    :return:
    """
    balance_info(user_obj['user_data'])
    if user_obj['user_data']['balance'] > 0:
        account_trans = input('\033[1;34;0mPlease input transfer to account>>\033[0m').strip()
        account_file = os.path.join(setting.DB_path, '%s.json' % account_trans)
        trans_account_data = db_handler.load_account_data(account_file)
        if trans_account_data:
            cash_trans = input('\033[1;34;0mPlease enter transfer cash>>\033[0m').strip()
            if cash_trans.isdigit():
                cash_trans = float(cash_trans)
                if 0 < cash_trans < user_obj['user_data']['balance']:
                    result_val = transaction.make_transaction(user_obj['user_data'], 'transfer', cash_trans)
                    if result_val:
                        result_val_rec = transaction.make_transaction(trans_account_data, 'transfer_rec', cash_trans)
                        if result_val_rec:
                            print(result_val)
                else:
                    msg = 'You number is not in a valid range!'
                    message_utils.print_error(msg)
            else:
                msg1 = 'Please enter a correct number'
                message_utils.print_error(msg1)
        else:
            msg2 = 'Wrong transfer account!'
            message_utils.print_error(msg2)
    else:
        msg3 = 'You balance is not enough to transfer!'
        message_utils.print_error(msg3)


# 管理接口
@decorator.login
def admin(user_obj, *args, **kwargs):
    """
提供管理接口，包括添加账户、用户额度，冻结账户等。。。
1.需要输入管理员账号，装饰器吗?
2. 调用bin/manage.py

    :param args:
    :param kwargs:
    :return:
    """
    if user_obj['user_data']['id'] == 'admin' and user_obj['user_data']['password'] == 'admin':
        manage.manage(user_obj)
    else:
        print('\033[1;30;0m')
        print('admin'.center(30, '-'))
        print('\033[0m')
        admin_user = input('\033[1;34;0m admin>>\033[0m')
        admin_password = input('\033[1;34;0m password>>\033[0m')
        user_data = auth.atm_authenticated(admin_user, admin_password)
        if user_data:
            decorator.user_obj['user_data'] = user_data
            manage.manage(user_obj)
        else:
            msg = 'Admin account error'
            message_utils.print_error(msg)


# 商城交易接口
@decorator.login
def mall_interface(user_obj, user, cash_total, *args):
    """

    :return:
    """
    ATM_account_date = user_obj['user_data']  # ATM 账号数据
    mall_account_data = user['user_data']  # 商城账户数据
    if ATM_account_date['balance'] > cash_total:  # 比较 ATM余额 和 消费总额
        settlement_result = transaction.make_transaction(ATM_account_date, 'consume', cash_total)
        if settlement_result:
            return [settlement_result, user_obj['user_data']['id']]
    else:
        msg = 'There is not enough balance'
        message_utils.print_error(msg)

