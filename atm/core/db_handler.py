#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 9:06
# @Author  : DolA
# @Site    : 
# @File    : db_handler.py
# @Software: PyCharm
import os
import json


# 根据用户账号找到存储账户数据的文件，把数据反序列化加载到内存
def load_account_data(account_file):
    """
 1、根据账号载入数据
        找到以car_num为文件名的账户文件car_num.json
            获取账户数据文件路径
        反序列化数据
    :return:
    """
    if os.path.isfile(account_file):
        with open(account_file, 'r', encoding='utf-8') as f:
            account_data = json.load(f)
            return account_data


# 将账户数据序列化
def json_data(user_data, file, status):
    if status == 1:   # status ==1 表示修改已存在账户文件中的数据 status == 0 表示创建新的文件
        if os.path.isfile(file):
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(user_data, f)
            return user_data
    if status == 0:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(user_data, f)
        return user_data
