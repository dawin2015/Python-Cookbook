#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 1_12.py
@time: 2019/1/5 14:03
"""

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)  # Output: [('eyes', 8), ('the', 5), ('look', 4)]

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

word_counts.update(morewords)

top_three = word_counts.most_common(3)
print(top_three)  # Output: [('eyes', 9), ('the', 5), ('look', 4)]
