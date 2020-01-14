import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:

    def setup_method(self):
        # browser = os.getenv("browser", "").lower()
        # print(browser)
        #
        # if browser == "phantomjs":
        #     self.driver = webdriver.PhantomJS()
        # elif browser == "firefox":
        #     self.driver = webdriver.Firefox()
        # elif browser == 'headless':
        #     options = webdriver.ChromeOptions()
        #     # 使用headless模式
        #     options.add_argument("--headless")
        #     options.add_argument("--disable-gpu")
        #     options.add_argument("--window-size=1280,1696")
        #
        #     self.driver = webdriver.Chrome(options=options)
        # elif browser == 'reuse':
        #     options = webdriver.ChromeOptions()
        #     # 使用已经存在的chrome进程
        #     #  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
        #     options.debugger_address = "127.0.0.1:9222"
        #     self.driver = webdriver.Chrome(options=options)
        # else:
        #     options = webdriver.ChromeOptions()
        #     # 使用已经存在的chrome进程
        #     #  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
        #     # options.debugger_address="127.0.0.1:9222"
        #     self.driver = webdriver.Chrome(options=options)
        #
        # if browser != 'reuse':
        #     self.driver.get("https://testerhome.com/")

        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        # 隐式等待，解决元素还未完成加载，找不到的问题，对所有的find element做等待
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # 显式等待
        # 使用LINK_TEXT会出现元素未加载完成出现的异常，可以使用CSS定位元素避免，尽量使用css的定位方法集

        element = (By.CSS_SELECTOR, '#teams .col-xs-12:nth-child(1) .team-name')
        self.wait(10, expected_conditions.visibility_of_element_located(element))
        # WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_elements(element)>1)
        # *element 因为find_element需要传两个参数，可以用*号把参数拆开
        self.driver.find_element(*element).click()
        # 使用css比link更好用
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def test_jinshuju(self):
        self.driver.get("https://testerhome.com/topics/21495")
        submit = (By.CSS_SELECTOR, ".published-form__submit")
        print(self.driver.window_handles)

        self.driver.switch_to.frame(0)
        self.wait(10, expected_conditions.element_to_be_clickable(submit))
        self.driver.find_element(*submit).click()

    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.set_window_size(1440, 877)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
        print(self.driver.window_handles)
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        element = (By.LINK_TEXT, '演讲申请')
        # self.driver.save_screenshot("1.png")
        self.wait(10, expected_conditions.presence_of_element_located(element))
        self.driver.find_element(*element).click()

    # def test_js(self):
    #     # todo: 专项测试的时候会讲如何获取性能
    #     for code in [
    #         "return document.title",
    #         'return document.querySelector(".active").className',
    #         'return JSON.stringify(performance.timing)'
    #     ]:
    #         result = self.driver.execute_script(code)
    #         print(result)

    # def test_shetuan(self):
    #     self.driver.find_element(By.CSS_SELECTOR, 'a[href="/teams"]').click()

    def teardown_method(self):
        sleep(5)
        self.driver.quit()
