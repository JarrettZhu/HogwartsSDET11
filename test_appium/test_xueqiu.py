# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["automationName"] = "uiautomator2"
        caps["deviceName"] = "test-avd"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["skipServerInstallation"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

        # 显式等待
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located())

    def test_search(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # el2.click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # # el3.send_keys("alibaba")
        # el3.send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_search_and_get_price_form_hk(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        gupiao = (By.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']")
        self.driver.find_element(*gupiao).click()
        price = (By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]")
        assert float(self.driver.find_element(*price).text) > 200

    def test_scroll(self):
        # 屏幕宽度高度
        size = self.driver.get_window_size()

        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2) \
                .release() \
                .perform()

    def test_device(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()

    def test_xpath(self):
        self.driver.find_element(By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current-price')]")

    def test_source(self):
        print(self.driver.page_source)

    def teardown(self):
        sleep(5)
        self.driver.quit()
