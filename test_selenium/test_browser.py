from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.test_hogwarts import TestHogwarts


class TestBrower(TestHogwarts):

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        # 隐式等待，解决元素还未完成加载，找不到的问题，对所有的find element做等待
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def teardown_method(self):
        sleep(5)
        self.driver.quit()
