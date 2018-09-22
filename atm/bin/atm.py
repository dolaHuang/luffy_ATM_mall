#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 9:04
# @Author  : DolA
# @Site    : 
# @File    : atm.py
# @Software: PyCharm

# 测试
# import os
# import sys
#
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 绝对路径
# sys.path.append(base_dir)
from atm.core import main


# 进入ATM
def atm_run():
    main.func_controller()

