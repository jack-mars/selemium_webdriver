from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/jackh/Downloads/chromedriver_win32/chromedriver')
#open the Url
driver.get('https://www.baidu.com/')
#maximize the browser
driver.fullscreen_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
#get title
BaiduTitle = driver.title
print(BaiduTitle)
#et Current Ural
CurrentUrl = driver.current_url
print(CurrentUrl)
#Browser Refresh
driver.refresh()
time.sleep(2)
#open another Url
driver.get("https://google.com")
#Browser Back
driver.back()
#Browser Forward
driver.forward()
#Get Page Source
pageSource = driver.page_source
print(pageSource)
driver.close()
#driver.quit()