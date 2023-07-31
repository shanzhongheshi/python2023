from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# 定义chrome驱动去地址
path =  Service('chromedriver.exe')

# 创建浏览器操作对象
browser = webdriver.Chrome(service=path)
# browser.get('https://www.baidu.com/')
#
browser.get('https://s.weibo.com/weibo/%25E5%25A5%25A5%25E8%25BF%2590%25E4%25BC%259A?topnav=1&wvr=6&b=11')
#

contents = browser.find_elements(By.XPATH,r'//li[@action-type="fl_pics"]')
print(contents)
print(len(contents))