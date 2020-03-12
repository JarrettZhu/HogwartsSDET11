from homework.appium_homework.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("bilibili")