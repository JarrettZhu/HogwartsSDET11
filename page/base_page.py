#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver


class BasePage:
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            # 允许每个类打开自己的地址
            self.driver.get(self._base_url)
        else:
            self.driver = driver
