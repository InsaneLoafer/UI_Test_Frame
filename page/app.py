import yaml
from appium import webdriver
from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        """
        复用driver，当driver为None时初始化driver；
        当driver不为None时直接启动activity
        :return:
        """
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "Insane"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            caps["udid"] = yaml.safe_load(open("../page/configuration.yaml"))["caps"]["udid"]
            # 初始化driver
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.start_activity(app_package=self._package, app_activity=self._activity)
        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main:
        return Main(self._driver)
