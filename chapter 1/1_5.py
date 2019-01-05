#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 1_5.py
@time: 2018/12/22 0:29
"""

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0


def push(self, item, priority):
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1


def pop(self):
    return heapq.heappop(self._queue)[-1]
