from homework.appium_homework.page.base_page import BasePage
from homework.appium_homework.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)
