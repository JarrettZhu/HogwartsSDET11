from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_appium.page.base_page import BasePage


class Search(BasePage):
    # todo:多平台、多版本、多个可能定位符（外部配置文件提取）
    _name_locator = (MobileBy.ID, "name")

    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(self._name_locator).click()
        return self

    def get_price(self, key: str) -> float:
        price = (By.XPATH, "//*[@text='%s']/../../..//*[contains(@resource-id, 'current_price')]" % key)
        return float(self._driver.find_element(*price).text)
