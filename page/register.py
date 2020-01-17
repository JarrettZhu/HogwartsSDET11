#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Register(BasePage):

    def register(self, corpname):
        self.driver.find_element(By.ID, 'corp_name').send_keys(corpname)
        self.driver.find_element(By.ID, 'submit_btn').click()
