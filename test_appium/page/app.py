from appium import webdriver
from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["automationName"] = "uiautomator2"
            caps["deviceName"] = "test-avd"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            # caps["dontStopAppOnReset"] = True
            # caps["unicodeKeyboard"] = True
            # caps["resetKeyboard"] = True
            # caps["skipServerInstallation"] = True
            # caps["chromedriverExecutableDir"] = '/Users/zhujunhua/Downloads/chromedriverdir'
            caps["chromedriverExecutable"] = '/Users/zhujunhua/Downloads/chromedriverdir/chromedriver_2.20'

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)
        else:
            print(self._driver)
            self._driver.start_activity(self._package, self._activity)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        # todo: wait main page
        return Main(self._driver)
