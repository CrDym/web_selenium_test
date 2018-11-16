# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 15:43
# @Author  : Cr
# @File    : myunit.py
import unittest
from driver import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        print('-----正在启动浏览器-----')
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        print('-----测试结束关闭浏览器-----')
        self.driver.quit()


