#-*-coding:utf-8-*-

import logging
import configparser
from selenium import webdriver
import time
import pytest

def test_zentao_login():
    logging.basicConfig(level=logging.DEBUG)

    logging.debug(u"读取配置文件")
    config = configparser.ConfigParser()
    config.read(r"./config/env.ini",encoding='utf-8')

    url = config.get('base','url')
    username = config.get('base','username')
    password = config.get('base','password')
    
    driver = webdriver.Chrome()   
    logging.debug(u"打开浏览器")        
    driver.implicitly_wait(5)
    driver.get(url)     
    driver.find_element_by_id("account").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("submit").click()

    time.sleep(5)
    #print (driver.title)
    assert driver.title == u"我的地盘 - 禅道"
    
    logging.debug(u"操作完成,关闭浏览器")    

    driver.close()
    driver.quit()

if __name__ == "__main__":
    pytest.main(['-s','-v','./testcases/test_zentao_login.py','--alluredir','./allure-results'])

   


    


    


