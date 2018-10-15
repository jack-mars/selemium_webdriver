from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/jackh/Downloads/chromedriver_win32/chromedriver')
# driver.fullscreen_window()
driver.get('http://google.com')
#driver.find_element_by_name('q').send_keys('inty python youtube\n')
driver.find_element_by_link_text("Gmail").click()
driver.back()
driver.find_element_by_partial_link_text("mail").click()