from appium import webdriver

from homework.appium_homework.page.base_page import BasePage
from homework.appium_homework.page.main import Main


class App(BasePage):

    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["automationName"] = "uiautomator2"
            caps["deviceName"] = "test-avd"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            # caps["noReset"] = True
            # caps["dontStopAppOnReset"] = True
            # caps["unicodeKeyboard"] = True
            # caps["resetKeyboard"] = True
            # caps["skipServerInstallation"] = True
            # caps["chromedriverExecutableDir"] = '/Users/zhujunhua/Downloads/chromedriverdir'
            caps["chromedriverExecutable"] = '/Users/zhujunhua/Downloads/chromedriverdir/chromedriver_2.20'

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self) -> Main():
        return Main(self._driver)
