#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 23:32
# @Author  : DolA
# @Site    : 
# @File    : admin_func.py
# @Software: PyCharm
import os
import time
import datetime
from atm.conf import setting
from atm.core import db_handler
from atm.core import logger
from atm.core import decorator
from atm.core import message_utils


# 添加账号
@decorator.login
def add_account(user, *args):
    """
    user_date:{'id': 888888, 'password': '1234', 'credit': 15000, 'balance': 15000, 'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01', 'pay_day': 22, 'status': 0}
    1.输入id
    2.输入password
    3.输入还款日
    4.自动设定 注册日期和有效日期
    5.根据id 创建 数据文件
    6.记录日志
    :return:
    """
    enroll_data = setting.account_dic  # 提取账号数据格式
    while True:
        enroll_data['id'] = input('\033[1;34;0mPlease enter a id what you want>>\033[0m').strip()
        if enroll_data['id'].isdigit() and len(enroll_data['id']) >= 6:
            file = os.path.join(setting.DB_path, '%s.json' % (enroll_data['id']))
            if not os.path.isfile(file):
                enroll_data['password'] = input('\033[1;34;0mPlease enter a password what you want>>\033[0m').strip()
                if 4 <= len(enroll_data['password']):   # 密码长度要求
                    enroll_data['pay_back'] = input('\033[1;34;0mPlease enter a date when you want to repay>>\033[0m').strip()
                    enroll_data['enroll_date'] = time.strftime('%Y-%m-%d')
                    enroll_data['expire_date'] = (
                                datetime.datetime.now() + datetime.timedelta(days=365 * 5 + 1)).strftime('%Y-%m-%d')
                    # 序列化
                    file = os.path.join(setting.DB_path, '%s.json' % (enroll_data['id']))
                    enroll_data = db_handler.json_data(enroll_data, file, status=0)
                    if enroll_data:
                        # 记日志
                        msg = 'admin %s add a account %s' % (user['user_data']['id'], enroll_data['id'])
                        log_file = os.path.join(setting.LOG_path, setting.LOG_TYPES['admin'])
                        logger.logger(log_file, msg)
                        msg1 = 'Add succeed!'
                        message_utils.print_succeed(msg1)
                        break
                    else:
                        msg2 = 'add failed!'
                        message_utils.print_error(msg2)
                else:
                    msg3 = 'The password must be greater than six!'
                    message_utils.print_error(msg3)
            else:
                msg4 = 'Account already exists,try another!'
                message_utils.print_error(msg4)
        else:
            msg5 = 'need a number that is at least six!'
            message_utils.print_error(msg5)


# 调整额度
@decorator.login
def adjust_credit(user ,*args):
    """
1.输入要调整的账号
2.输入调整 大小
3.修改数据，保存
4.记录日志
    :param user:
    :return:
    """
    while True:
        # 根据输入的账号 查找 并反序列化
        adjust_account = input('\033[1;34;0m Enter a ID which you want adjust>>\033[0m').strip()
        account_file = os.path.join(setting.DB_path, '%s.json' % adjust_account)
        adjust_data = db_handler.load_account_data(account_file)
        if adjust_data:
            new_credit = input('\033[1;34;0mPlease enter a new cash of credit>>\033[0m').strip()
            if new_credit.isdigit():
                new_credit = float(new_credit)
                if 0 < new_credit:
                    adjust_data['credit'] = new_credit
                    # 序列化
                    file = os.path.join(setting.DB_path, '%s.json' % (adjust_data['id']))
                    adjust_data = db_handler.json_data(adjust_data, file, status=1)
                    if adjust_data:
                        # 记日志
                        msg = 'admin %s adjust credit for account %s' % (user['user_data']['id'], adjust_account)
                        log_file = os.path.join(setting.LOG_path, setting.LOG_TYPES['admin'])
                        logger.logger(log_file, msg)
                        msg1 = 'Adjust succeed'
                        message_utils.print_succeed(msg1)
                        break
                    else:
                        msg2 = 'Adjust failed!'
                        message_utils.print_error(msg2)
                else:
                    msg3 = 'Enter a wrong credit!'
                    message_utils.print_error(msg3)
            else:
                msg4 = 'Need a number here!'
                message_utils.print_error(msg4)
        else:
            msg5 = 'Non-existent account'
            message_utils.print_error(msg5)


# 冻结账户
@decorator.login
def frozen_account(user, *args):
    """
    冻结就是使账户无法登陆
    把status 赋值成 -1
    :param user:
    :return:
    """
    frozen_acc = input('\033[1;34;0mEnter a ID which you want frozen>>\033[0m').strip()
    # 根据输入的账号 反序列化
    account_file = os.path.join(setting.DB_path, '%s.json' % frozen_acc)
    frozen_data_old = db_handler.load_account_data(account_file)
    if frozen_data_old:
        if frozen_data_old['status'] == -1:
            msg1 = 'This account has been frozen before!'
            message_utils.print_error(msg1)
        elif frozen_data_old['status'] == 0:
            frozen_data_old['status'] = -1
            # 序列化
            file = os.path.join(setting.DB_path, '%s.json' % (frozen_data_old['id']))
            frozen_data = db_handler.json_data(frozen_data_old, file, status=1)
            if frozen_data:
                # 记日志
                msg = 'admin %s frozen account %s' % (user['user_data']['id'], frozen_acc)
                log_file = os.path.join(setting.LOG_path, setting.LOG_TYPES['admin'])
                logger.logger(log_file, msg)
                msg2 = 'frozen succeed!'
                message_utils.print_succeed(msg2)

