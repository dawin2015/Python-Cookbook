#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 2_6.py
@time: 2019/1/6 14:58
"""

import re


# 支撑函数
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


text = 'UPPER PYTHON, lower python, Mixed Python'

result = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(result)
