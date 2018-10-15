from selenium import webdriver

driver = webdriver.Chrome('C:/Users/jackh/Downloads/chromedriver_win32/chromedriver')
# driver.fullscreen_window()
driver.get('http://baidu.com')
elments = driver.find_elements_by_tag_name('a')
for elment in elments:
    #print(elment.text)
    if '新闻' in elment.text:
        elment.click()
#driver.quit()