from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

# url地址
url = 'http://www.baidu.com'

# 定义chrome驱动去地址
path =  Service('chromedriver.exe')

# 创建浏览器操作对象
browser = webdriver.Chrome(service=path)

time.sleep(3)

browser.get(url)
print(browser.title)