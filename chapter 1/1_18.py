#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 1_18.py
@time: 2019/1/5 21:22
"""

from collections import namedtuple

# example 1
# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# sub = Subscriber('jonesy@example.com', '2012-10-19')
# print(sub)

# example 2
# Stock = namedtuple('Stock', ['name', 'shares', 'price'])
#
#
# def compute_cost(records):
#     total = 0.0
#     for rec in records:
#         s = Stock(*rec)
#         total += s.shares + s.price
#     return

# example 3: namedtuple是不可变的, 使用namedtuple实例的_replace()方法修改属性, 也可以作为一种简便的方法
# 填充具有可选或缺失字段的命名元祖
Stock = namedtuple('Stock', ['name', 'share', 'price', 'date', 'time'])
# 创建一个包含默认值的原型元组
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)

