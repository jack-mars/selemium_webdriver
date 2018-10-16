from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/jackh/Downloads/chromedriver_win32/chromedriver')
driver.get('https://www.baidu.com/')
driver.find_element_by_css_selector("#kw").send_keys("inty youtube\n")
#return
