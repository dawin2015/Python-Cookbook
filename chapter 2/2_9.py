#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 2_9.py
@time: 2019/1/6 17:16
"""

import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1 == s2)
print(s1)
print(s2)

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)

print(t1 == t2)
print(ascii(t1))
print(ascii(t2))
