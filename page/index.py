#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.register import Register


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        return Register(self.driver)
