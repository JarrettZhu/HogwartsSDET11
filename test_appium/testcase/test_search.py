import pytest
import yaml

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_search_page().search("alibaba").get_price("BABA") > 200

    def test_select(self):
        assert "已添加" in self.main.goto_search_page().search("jd").add_select().get_msg()

    # @pytest.mark.parametrize("key, stock_type, price", [
    #     ("alibaba", "BABA", 200),
    #     ("JD", "JD", 20)
    # ])

    @pytest.mark.parametrize("key, stock_type, price", yaml.safe_load(open("data.yaml")))
    def test_search_data(self, key, stock_type, price):
        assert self.main.goto_search_page().search(key).get_price(stock_type) > price

    @pytest.mark.parametrize("code, name", [
        ("jd", "京东"),
        ("alibaba", "阿里巴巴")
    ])
    def test_stocks(self, code: str, name: str):
        """
        作业一：进入行情页，搜索股票并添加自选，然后重新回到行情页。
        """
        text = self.main.goto_stocks().goto_search_page_from_stocks().search(code).add_select().cancel().get_name()
        assert name in text
