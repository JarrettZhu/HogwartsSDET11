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
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["skipServerInstallation"] = True
        # caps["chromedriverExecutableDir"] = '/Users/zhujunhua/Downloads/chromedriverdir'
        caps["chromedriverExecutable"] = '/Users/zhujunhua/Downloads/chromedriverdir/chromedriver_2.20'

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

    def test_webview(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        phone = (MobileBy.XPATH, "//android.widget.EditText")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(phone))
        # sleep(10)
        # print(self.driver.page_source)
        # print(self.driver.find_element(*phone).get_attribute("content-desc"))
        self.driver.find_element(*phone).click()
        self.driver.find_element(*phone).send_keys('13424103317')
        # todo

    def test_webview_context(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        for i in range(5):
            print(self.driver.contexts)
            sleep(0.5)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        phone = (MobileBy.XPATH, "//android.widget.EditText")
        self.driver.find_element(*phone).click()
        self.driver.find_element(*phone).send_keys('13424103317')

    def test_xueying(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        # 判断上下文内容是否大于1，大于1则代表webview出现
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        # 切换至新出现的上下文内容
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR, '.trade_home_xueying_SJY .trade_home_info_3aI').click()
        # 打印当前存在的窗口
        for i in range(5):
            print(self.driver.window_handles)
            sleep(1)
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        # 切换至最后出现的窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phonenum = (By.CSS_SELECTOR, '.open_input-wrapper_13S > input[placeholder*="手机号"]')
        self.driver.find_element(*phonenum).send_keys('13424103317')
        self.driver.find_element(By.CSS_SELECTOR, '.open_input-wrapper_13S > input[placeholder*="验证码"]').send_keys(
            '1234')
        self.driver.find_element(By.CSS_SELECTOR, '.open_form-submit_1Ms').click()

    def teardown(self):
        sleep(5)
        self.driver.quit()
