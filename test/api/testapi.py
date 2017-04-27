#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wang jing'
import unittest


class testApi(unittest.TestCase):
    '''
    单元测试的写法
    '''

    def test_key(self):
        d = 5
        self.assertEquals(d, 5)


if __name__ == '__main__':
    unittest.main()
