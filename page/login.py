#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.register import Register


class Login(BasePage):
    def scan_qrcode(self):
        pass

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '企业注册').click()
        return Register(self._driver)
