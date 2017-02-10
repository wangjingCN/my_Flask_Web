#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
__author__ = 'wang jing'
'''实际上就是python的getter和setter方法'''

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


s = Student()
s.birth = 20
print s.age
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
print Chain().ag.add.list
logging.exception('')