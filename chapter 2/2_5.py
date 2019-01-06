#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 2_5.py
@time: 2019/1/6 14:47
"""

import re

text = 'Today is 11/27/2012, PyCon starts 3/13/2012'
result = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(result)

