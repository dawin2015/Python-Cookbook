#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 2_2.py
@time: 2019/1/6 14:24
"""

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatchcase('foo.txt', '*.TXT'))
