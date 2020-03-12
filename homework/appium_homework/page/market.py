from homework.appium_homework.page.base_page import BasePage
from homework.appium_homework.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)
