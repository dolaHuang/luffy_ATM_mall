#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 12:08
# @Author  : DolA
# @Site    : 
# @File    : home.py
# @Software: PyCharm
import os
import sys
from atm.core import message_utils
base_dir = os.path.dirname(os.path.abspath(__file__))  # 绝对路径
sys.path.append(base_dir)


def home():
    while True:
        print(info)
        choice_home = input('\033[1;34;0menter your choice>>\033[0m').strip()
        if choice_home == '1':
            shopping_mall.run_mall()
        elif choice_home == '2':
            # atm.atm_run()
            atm.atm_run()
        elif choice_home == '3':
            exit('bye')
        else:
            msg = 'error enter!'
            message_utils.print_error(msg)


# 启动程序
if __name__ == '__main__':
    from atm.bin import atm
    from shopping_mall.bin import shopping_mall

    info = """\033[1;36;0m
*==*== Luffy Shopping ATM ==*==*
    1>Luffy  Shopping mall
    2>ATM
    3>exit
*==*==*==*==*==*==*==*==*==*==*
    \033[0m"""
    home()
