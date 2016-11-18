#!/usr/bin/env python
# -*- coding: utf-8 -*-
class A:
    def __init__(self, result='success', message="", data=[]):
        self.result = result
        self.message = message
        self.data = data

    def __repr__(self):
        return str(dict(result=self.result, message=self.message, data=self.data))


a = A(message="", data=[1, 2])
print a
