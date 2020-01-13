from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        # 隐式等待，解决元素还未完成加载，找不到的问题
        self.driver.implicitly_wait(5)

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        sleep(1)
        # todo:显示等待
        self.driver.find_element(By.LINK_TEXT, '霍格沃兹测试学院').click()
        # todo:隐式等待
        self.driver.find_element(By.CSS_SELECTOR, 'css=.topic-21072 .title > a').click()

    def teardown_method(self):
        sleep(20)
        self.driver.quit()
