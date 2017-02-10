#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class AuthLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.client = webdriver.Firefox()
        self.client.maximize_window()
        self.client.get('http://127.0.0.1:5000/auth/login')
        time.sleep(2)
        self.client.find_element_by_name('userName').send_keys('admin')
        time.sleep(2)
        self.client.find_element_by_id('password').send_keys('admin')
        time.sleep(2)
        self.client.find_element_by_tag_name('button').click()
        
    def testbaidu(self):
        print self.client.title
        self.client.get('http://127.0.0.1:5000/change/ltm/standard-service-upline')
        #对没有name和id属性的元素，则用xpath
        self.client.find_element_by_xpath('//input[@placeholder="请输入服务名称"]').send_keys('wwww.cmbchina.com')
        self.client.find_element_by_xpath('//input[@placeholder="服务器地址"]').send_keys('10.1.0.16')
        self.client.find_element_by_xpath('//button[@ng-click="addRealServerList()"]').click()
        # self.assertTrue(self.client.find_element_by_xpath('//button[@ng-click="addRealServerList()"]').is_selected())
        self.client.find_element_by_xpath('//input[@value="TCP_PORT"]').click()
        print self.client.title


if __name__ == "__mian__":
    unittest.main()
