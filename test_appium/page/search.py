from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_appium.page.base_page import BasePage
from test_appium.page.stocks import Stocks


class Search(BasePage):
    # todo:多平台、多版本、多个可能定位符（外部配置文件提取）
    _name_locator = (MobileBy.ID, "name")

    def search(self, key: str):
        # self.find(MobileBy.ID, "search_input_text").send_keys(key)
        # self.find(self._name_locator).click()
        self._params = {}
        self._params["key"] = key
        self.steps("../page/search.yaml")

        return self

    def get_price(self, key: str) -> float:
        price = (By.XPATH, "//*[@text='%s']/../../..//*[contains(@resource-id, 'current_price')]" % key)
        return float(self._driver.find_element(*price).text)

    def add_select(self):
        element = self.find_by_test("加自选")
        element.click()
        return self

    def un_select(self):
        element = self.find_by_test("已添加")
        element.click()
        return self

    def get_msg(self):
        return self.find_and_get_text(By.ID, "followed_btn")

    def cancel(self) -> Stocks:
        self.find_by_id("action_close").click()
        return Stocks(self._driver)
