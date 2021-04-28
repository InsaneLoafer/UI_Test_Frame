import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    # 定义driver实例变量
    _driver: WebDriver = None

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        return self._driver.find_element(locator, value)


    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step[ "action"]
                    if action == "click":
                        element.click()
