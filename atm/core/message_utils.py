#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 9:40
# @Author  : DolA
# @Site    : 
# @File    : message_utils.py
# @Software: PyCharm


# 打印字体高亮显示
def print_enter(msg):
    print('\033[1;34;0m%s\033[0m' % msg)


def print_error(msg):
    print('\033[1;31;0m Error:%s\033[0m' % msg)


def print_info(msg):
    print('\033[1;36;0m%s\033[0m' % msg)


def print_succeed(msg):
    print('\033[1;36;0m%s\033[0m' % msg)