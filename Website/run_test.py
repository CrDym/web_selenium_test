# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 13:45
# @Author  : Cr
# @File    : run_test.py
import unittest
from function import *
from HTMLTestRunner import HTMLTestRunner
import time

report_dir = './test_report'
test_dir = './test_case'

print('-----开始执行测试用例-----')
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_login.py")

now = time.strftime("%Y-%m-%d %H-%M-%S")
report_name = report_dir+'/'+now+'result.html'

print('-----开始生成测试报告-----')
with open(report_name,'wb') as f:
    runner = HTMLTestRunner(stream=f,
                          title="Test Reprot",
                          description="Login test")
    runner.run(discover)
    f.close()

print('查找最新报告')
latest_report= latest_report(report_dir)

print('发送测试报告')
send_mail(latest_report)

print('-----测试已完成-----')