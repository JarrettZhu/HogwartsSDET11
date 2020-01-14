#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_hogwarts(self):
        self.driver.find_element(By.CSS_SELECTOR, '.topic-21805 .title > a').click()
        self.driver.find_element(By.CSS_SELECTOR, '.btn > .caret').click()
        self.driver.find_element(By.CSS_SELECTOR, '.toc-item:nth-child(4) > .toc-item-link').click()

    def teardown_method(self):
        sleep(5)
        self.driver.quit()
