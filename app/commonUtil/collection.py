#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple

__author__ = 'wang jing'
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x

from collections import deque

a = ['x', 'y', 'z']
print a

deque_param = deque(a)
print deque_param
deque_param.append('a')
deque_param.appendleft('b')
print deque_param

import base64

a = base64.b64encode('binary string')
print a
print base64.b64decode('YmluYXJ5AHN0cmluZw==')

import hashlib

md = hashlib.md5()
md.update('Do you love me ?')
md.update('yes')
print md.hexdigest()

hs = hashlib.sha1()
hs.update('Do you love me ?')
hs.update('yes')
print hs.hexdigest()

import itertools

itertools.count(1)
itertools.cycle('adb')
itertools.repeat('a', 10)
