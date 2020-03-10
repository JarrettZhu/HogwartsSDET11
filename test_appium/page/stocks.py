from test_appium.page.base_page import BasePage


class Stocks(BasePage):
    def goto_search_page_from_stocks(self):
        """
        从行情页进入
        """
        # 导入语句放在顶部会导致循环导入报错，先放在这里防止出现循环导入错误
        from test_appium.page.search import Search
        self.find_by_id("action_search").click()
        return Search(self._driver)

    def get_name(self):
        """
        获取
        """
        return self.find_by_id("portfolio_stockName").text
