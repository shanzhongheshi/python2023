import re  # 正则表达式提取文本
import requests  # 爬虫发送请求
from bs4 import BeautifulSoup as BS  # 爬虫解析页面
import time
import pandas as pd  # 存入csv文件
import os
import snownlp
import matplotlib.pyplot as plt
import jieba.analyse
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
    # print('{}:{}'.format(danmu_time, d.text))
v_result_file='本草纲目.csv'
if os.path.exists(v_result_file):
    header=None
else:
    header=['视频地址','弹幕地址','弹幕时间','弹幕内容','情感得分','分析结果']

c={"video_url":video_url_list,
   "danmu_url":danmu_url_list,
   "time":time_list,
   "text":text_list}
df=pd.DataFrame(c)


# 情感判定
score_list=[]
tag_list=[]
neg_count=0
pos_count=0
mid_count=0
for comment in text_list:
    tag = ''
    sentiments_score = snownlp.SnowNLP(comment).sentiments
    if sentiments_score < 0.5:
        tag = '消极'
        neg_count += 1
    elif sentiments_score > 0.5:
        tag = '积极'
        pos_count += 1
    else:
        tag = '中性'
        mid_count += 1
    score_list.append(sentiments_score)  # 得分值
    tag_list.append(tag)  # 判定结果
df['情感得分'] = score_list
df['分析结果'] = tag_list
print(df)
# df.to_csv(v_result_file,encoding='utf_8_sig',mode="a+",index=False,header=header)

grp = df['分析结果'].value_counts()
print('正负面评论统计：')
print(grp)
grp.plot.pie(y='分析结果', autopct='%.2f%%')  # 画饼图
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
plt.title('刘畊宏弹幕_情感分布占比图')
plt.savefig('刘畊宏弹幕_情感分布占比图.png')  # 保存图片
# 2、用jieba统计弹幕中的top10高频词
keywords_top10 = jieba.analyse.extract_tags(text_list.__str__(), withWeight=True, topK=10)
print('top10关键词及权重：')
print(keywords_top10)