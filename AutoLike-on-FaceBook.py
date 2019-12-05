# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
# input email and password
driver.find_element_by_name("email").send_keys("email")
driver.find_element_by_name("pass").send_keys("password")
# click the login button
driver.find_element_by_css_selector('input[value="登录"]').click()
Like_Counter = 0
for Like_Counter in range(0,100000000,1):
#clike the Like Button
  driver.find_elements_by_css_selector('div[class="_666k"]')[Like_Counter].click()
  time.sleep(0.1)
  driver.execute_script("window.scrollBy(0,3000)")
  Like_Counter=Like_Counter+1
# screenshot the login website
driver.save_screenshot("renren.png")
