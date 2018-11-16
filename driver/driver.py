# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 15:40
# @Author  : Cr
# @File    : driver.py
from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()

    # driver.get('http://www.baidu.com')

    return driver

if __name__ == '__main__':
    browser()