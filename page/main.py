
from page.base_page import BasePage

class Main(BasePage):
    def goto_search(self):
        """
        进入搜索
        :return:
        """
        # self.find(By.ID, "tv_search").click()
        self.steps("../page/main.yaml")