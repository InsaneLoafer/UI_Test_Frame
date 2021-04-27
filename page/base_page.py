from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 定义driver实例变量
    _driver: WebDriver = None

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        return self._driver.find_element(locator, value)
