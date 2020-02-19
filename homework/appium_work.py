from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestXueqiuHomework:
    """
    作业三
    添加某只股票到自选，然后再次搜索并验证，股票已经加入自选。（不要使用文字内容判断，使用get attribute）
    """
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["automationName"] = "uiautomator2"
        caps["deviceName"] = "test-avd"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_follow_by_self(self, equity_num: str = "00700"):
        """
        测试添加自选股票
        :param equity_num: 股票代码，默认值为"00700"腾讯控股
        """
        # 首次进入要点击同意按钮
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # 点击搜索编辑框
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys(equity_num)
        self.driver.find_element(MobileBy.ID, "name").click()
        # 点击股票
        equity = (By.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']")
        self.driver.find_element(*equity).click()
        # 点击加自选按钮
        follow_button = (By.XPATH, "//*[@text='%s']/../../..//*[contains(@resource-id, 'follow_btn')]" % equity_num)
        self.driver.find_element(*follow_button).click()
        # 点击下次再说按钮
        self.driver.find_element(MobileBy.ID, "tv_left").click()
        # 点击取消按钮，返回首页
        self.driver.find_element(MobileBy.ID, 'action_close').click()

        # 再次搜索已加入自选的股票
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys(equity_num)
        self.driver.find_element(MobileBy.ID, "name").click()

        # 定义列表用于存放查找到的resource-id元素，用于断言
        resourceid_list = []
        # 根据股票代码元素的父节点查找父节点下的resource-id结果集
        for e in self.driver.find_elements(By.XPATH, "//*[@text='%s']/../../..//*[@resource-id]" % equity_num):
            # 遍历结果集，根据"/"分割出resource-id
            resourceid_list.append(e.get_attribute("resource-id").split('/')[1])
        # 打印列表长度
        print(len(resourceid_list))
        # 断言resource-id是否为"followed_btn"，该id表示改股票已加入自选（未加入自选的股票该按钮resource-id为"follow_btn"）
        assert "followed_btn" in resourceid_list

    def teardown(self):
        self.driver.quit()
