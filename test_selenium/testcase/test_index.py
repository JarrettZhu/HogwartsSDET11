#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(3)
        # self.driver.get("https://work.weixin.qq.com/")
        # self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        # self.driver.find_element(By.ID, 'corp_name').send_keys("科大讯飞")
        # self.driver.find_element(By.ID, 'submit_btn').click()

        self.index.goto_register().register("科大讯飞")

    def test_login(self):
        register_page = self.index.goto_login().goto_register().register("科技有限公司")
        print(register_page.get_error_message())
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
