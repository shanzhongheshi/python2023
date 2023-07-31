import re  # 正则表达式提取文本
import requests  # 爬虫发送请求
from bs4 import BeautifulSoup as BS  # 爬虫解析页面
import time
import pandas as pd  # 存入csv文件
import os
v_url='https://www.bilibili.com/video/BV1Pa411v7vg'
cid='574147025'
# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}
#http://comment.bilibili.com/574147025.xml
danmu_url = 'http://comment.bilibili.com/{}.xml'.format(cid)  # 弹幕地址
print('弹幕地址是：', danmu_url)
r2 = requests.get(danmu_url,headers=headers)
print(r2.apparent_encoding)
# 调用.encoding属性获取requests模块的编码方式
# 调用.apparent_encoding属性获取网页编码方式
# 将网页编码方式赋值给response.encoding
r2.encoding=r2.apparent_encoding
html2=r2.text
print(html2)
soup = BS(html2, 'xml')
danmu_list = soup.find_all('d')
print('共爬取到{}条弹幕'.format(len(danmu_list)))
print(danmu_list)
video_url_list = []  # 视频地址
danmu_url_list = []  # 弹幕地址
time_list = []  # 弹幕时间
text_list = []  # 弹幕内容
for d in danmu_list:
    data_split = d['p'].split(',')  # 按逗号分隔
    temp_time = time.localtime(int(data_split[4]))  # 转换时间格式
    danmu_time = time.strftime("%Y-%m-%d %H:%M:%S", temp_time)
    video_url_list.append(v_url)
    danmu_url_list.append(danmu_url)
    time_list.append(danmu_time)
    text_list.append(d.text)
    print('{}:{}'.format(danmu_time, d.text))
v_result_file='本草纲目.csv'
if os.path.exists(v_result_file):
    header=None
else:
    header=['视频地址','弹幕地址','弹幕时间','弹幕内容']

c={"video_url":video_url_list,
   "danmu_url":danmu_url_list,
   "time":time_list,
   "text":text_list}
df=pd.DataFrame(c)
print(df)
df.to_csv(v_result_file,encoding='utf_8_sig',mode="a+",index=False,header=header)

