# 时间 2020/12/9 22:54
from Base.Base import Base
from Page import *


class Add_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def add_user_click(self):
        self.click_element(add_user_btn)

    def save_loc_click(self):
        self.click_element(save_loc)
