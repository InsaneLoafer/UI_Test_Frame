import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    # 定义driver实例变量
    _driver: WebDriver = None
    # 定义弹窗黑名单
    _black_list = [(By.ID, "iv_close")]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        """
        定义find方法，并解决弹窗问题
        :param locator:
        :param value:
        :return:
        """
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            """
            弹窗处理：遍历弹窗黑名单，如果黑名单列表长度大于0则每次点击第一个元素
            点击完成后退出循环，然后返回find()方法，再次找原来的元素
            """
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator, value)



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
