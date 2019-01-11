#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 4_15.py
@time: 2019/1/11 23:28
"""

import heapq


with open('sorted_file1', 'rt') as file1, open('sorted_file2', 'rt') as file2, open('merged_list', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)