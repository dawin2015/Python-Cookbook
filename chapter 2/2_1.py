#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 2_1.py
@time: 2019/1/6 14:09
"""

import re

line = 'asdf fjdk; afed, fjek,asdf,    foo'

result = re.split(r'[;,\s]\s*', line)
print(result)