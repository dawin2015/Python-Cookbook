#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 3.6
@author: dawin
@contact: 694596886@qq.com
@site: https://blog.csdn.net/dawin_2008
@software: PyCharm
@file: 4_13.py
@time: 2019/1/11 22:51
"""

import os
import fnmatch
import gzip
import bz2
import re


def gen_file(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    :param filepat:
    :param top:
    :return:
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    :param filename:
    :return:
    '''
    for filename in filenames:
        if filename.endwith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endwith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'r')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
    Chain a sequence of iterations together into a single sequence.
    :param iterators:
    :return:
    '''
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    :param pattern:
    :param lines:
    :return:
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

