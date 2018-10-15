from selenium import webdriver

driver = webdriver.Chrome('C:/Users/jackh/Downloads/chromedriver_win32/chromedriver.exe')
driver.fullscreen_window()
driver.get('http://baidu.com')
driver.find_element_by_id("kw").send_keys('China')
driver.save_screenshot("C:/Users/jackh/Desktop/截图.png")
driver.close()

