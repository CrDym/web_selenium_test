# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 16:40
# @Author  : Cr
# @File    : test_login.py
import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import sleep


class LoginTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login1_normal(self):
        '''用户名及密码正确'''
        print('test_login1_normal is start test...')
        po= LoginPage(self.driver)
        po.Login_action('cherong','123456')
        sleep(3)

        self.assertEqual(po.type_loginPass_hint(),'我的空间')
        function.insert_img(self.driver,'login_normal.png')
        print('test_login1_normal test end!')

    # @unittest.skip('skip this case')
    def test_login2_PasswdError(self):
        '''密码错误'''
        print('test_login2_passwderror is start test...')
        po= LoginPage(self.driver)
        po.Login_action('cherong','111111')
        sleep(3)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,'login_passwderror.png')
        print('test_login2_passwderror test end!')

    # @unittest.skip('skip this case')
    def test_login3_empty(self):
        '''用户名和密码为空'''
        print('test_login3_empty is start test...')
        po= LoginPage(self.driver)
        po.Login_action('','')
        sleep(3)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,'login_empty.png')
        print('test_login2_empty test end!')


if __name__ == '__main__':
    unittest.main()