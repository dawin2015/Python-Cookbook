#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 1_14.py
@time: 2019/1/5 20:14
"""

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


user = [User(23), User(3), User(99)]



result = sorted(user, key=attrgetter('user_id'))
print(result)
result = min(user, key=attrgetter('user_id'))
print(result)
result = max(user, key=attrgetter('user_id'))
print(result)