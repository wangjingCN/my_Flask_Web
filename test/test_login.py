#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class SeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.client = webdriver.Firefox()
        self.client.get('https://exmail.qq.com/cgi-bin/loginpage')
        time.sleep(2)
        self.client.find_element_by_name('inputuin').send_keys('wangjing@gzsunrun.cn')
        time.sleep(2)
        self.client.find_element_by_id('pp').send_keys('Sr12345')
        time.sleep(2)
        self.client.find_element_by_id('btlogin').click()

    # def testxinlang(self):
    #     self.client.get('https://www.baidu.com')
    #     print self.client.title
    #     self.client.get('https://exmail.qq.com/cgi-bin/loginpage')
    #     print self.client.title

    def testbaidu(self):
        print self.client.title
        self.client.get(
            'https://exmail.qq.com/cgi-bin/frame_html?sid=KiQBHV19u2f76lkB,7&r=413e2243e4f7c556f3e36b1084dac37b')
        print self.client.title


if __name__ == "__mian__":
    unittest.main()
