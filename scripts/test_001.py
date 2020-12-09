import os,sys
sys.path.append(os.getcwd())

import pytest
import allure
from Page.Page_Obj import Page_Obj
from Base.Driver import init_driver
from Page.Page_do import Add_Page


# class Test_Abc():
#
#     @allure.step(title='第一个测试')
#     @allure.severity(allure.severity_level.TRIVIAL)
#     def test_001(self):
#         allure.attach("这是一个描述","试一下")
#         assert 1
#
#     @allure.issue('http://www.baidu.com')
#     @allure.testcase("http://www.baidu.com/test_001")
#     @allure.severity(allure.severity_level.TRIVIAL)
#     def test_002(self):
#         allure.attach("这是第二个描述",'....')
#         assert 0
class Test_A():
    def setup_class(self):
        self.driver = init_driver()
        self.add_user_obj = Page_Obj(self.driver).return_Page_do()

    def teardown_class(self):
        self.driver.quit()

    def test_001(self):
        self.add_user_obj.add_user_click()
        self.add_user_obj.save_loc_click()
        assert 1
