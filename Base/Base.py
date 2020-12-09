# 时间 2020/12/9 22:30
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver
    def find_element_o(self,loc):
       return WebDriverWait(self.driver,timeout=10,poll_frequency=0.5)\
           .until(lambda x: x.find_element_o(*loc))
    def click_element(self,loc):
        self.find_element_o(loc).click()
    def input_element(self,loc,text):
        inp = self.find_element_o(loc)
        inp.clear()
        inp.send_key(text)