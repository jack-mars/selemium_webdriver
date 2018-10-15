from selenium import webdriver

driver = webdriver.Chrome('C:/Users/jackh/Downloads/chromedriver_win32/chromedriver')
driver.fullscreen_window()
driver.get('http://amazon.com')
driver.find_element_by_id("nav-your-amazon").click()