#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # “driver: WebDriver” 指定driver类型为WebDriver
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            # 允许每个类打开自己的地址
            self._driver.get(self._base_url)
        else:
            self._driver = driver

    def close(self):
        sleep(20)
        self._driver.quit()
