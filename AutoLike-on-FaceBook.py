# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
# driver.get("http://oa.gaei.cn/seeyon/")
driver.get("https://www.facebook.com/")
# driver.fullscreen_window()
# # # 输入账号密码
# # driver.find_elements_by_name("login_username").send_keys("gz04825")
# # driver.find_elements_by_name("login_password").send_keys("ysq1159889481")
driver.find_element_by_name("email").send_keys("+86 18629286360")
driver.find_element_by_name("pass").send_keys("ysq1159889481")
# 模拟点击登录
# driver.find_elements_by_css_selector('input[id="login_button"]').click()
driver.find_element_by_css_selector('input[value="登录"]').click()
Like_Counter = 0
for Like_Counter in range(0,100000000,1):
  driver.find_elements_by_css_selector('div[class="_666k"]')[Like_Counter].click()
  time.sleep(0.1)
  driver.execute_script("window.scrollBy(0,3000)")
  Like_Counter=Like_Counter+1
# 生成登陆后快照
# driver.save_screenshot("renren.png")