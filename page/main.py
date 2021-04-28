from selenium.webdriver.common.by import By

from page.base_page import BasePage

class Main(BasePage):
    def goto_search(self):
        """
        进入搜索
        :return:
        """
        # self.find(By.ID, "tv_search").click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        # 点击写文章按钮，此时会有进行登录的弹窗
        self.find(By.ID, "post_status").click()
        # 自动处理弹窗，然后点击搜索按钮
        self.find(By.ID, "tv_search").click()