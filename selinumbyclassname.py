from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/jackh/Downloads/chromedriver_win32/chromedriver')
driver.get('https://www.douban.com/')
driver.find_element_by_class_name('lnk-movie').click()