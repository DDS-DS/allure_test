# 时间 2020/12/9 22:59
from Page.Page_do import Add_Page


class Page_Obj():
    def __init__(self, driver):
        self.driver = driver

    def return_Page_do(self):
        return Add_Page(self.driver)
