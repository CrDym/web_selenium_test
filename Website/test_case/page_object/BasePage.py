# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 16:13
# @Author  : Cr
# @File    : BasePage.py
from time import sleep

class Page():
    def __init__(self,driver):
        self.driver = driver
        self.base_url='http://localhost'
        self.timeout = 10

    def _open(self,url):
        url_=self.base_url+url
        print('Test page is %s '%url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_,'Did not land on %s'%url_

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
