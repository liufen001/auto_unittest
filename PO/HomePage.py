#coding=utf-8
from selenium import webdriver
from time import sleep
from Libs.log_utils import TSlog
import logging

class baidusearch():
    def __int__(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def login(self,name,pwd):

        self.driver.find_element_by_id('loginname').clear()
        self.driver.find_element_by_id('loginname').send_keys(name)
        sleep(1)
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(pwd)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span').click()


    def page_should_contain(self,text):
        self.driver.implicitly_wait(10)
        xpath="//*[contains(text(),'%s')]"%text
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            TSlog.Error('页面找不到对象')
            return False
        TSlog.Info('页面加载成功')
        return True

    def bclose(self):
        self.driver.close()






