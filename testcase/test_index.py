#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from page.index import Index


class TestIndex:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/")

    def test_register(self):
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(3)
        # self.driver.get("https://work.weixin.qq.com/")
        # self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        # self.driver.find_element(By.ID, 'corp_name').send_keys("科大讯飞")
        # self.driver.find_element(By.ID, 'submit_btn').click()

        index = Index(self.driver)
        index.goto_register().register("科大讯飞")
