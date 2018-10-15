from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome('C:/Users/jackh/Downloads/chromedriver_win32/chromedriver')
driver.fullscreen_window()
driver.get('http://www.timeanddate.com')
selectElements = driver.find_element_by_id("month")
months = Select(selectElements)
months.select_by_visible_text("December")
countriesElements = driver.find_element_by_id("country")
countries = Select(countriesElements)
countries.select_by_visible_text("Taiwan")
driver.find_element_by_xpath("//form[@id='cf']//input[@value='View Calendar']").click()