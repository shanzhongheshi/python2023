import requests
from pprint import pprint
import requests_cache  #缓存
import time   #请求完要睡眠
import  os #写入到文件
import pandas as pd
import sqlalchemy  #将pandas的df写入到mysql库
import datetime   #处理微博时间

requests_cache.install_cache()
requests_cache.clear()
#正则匹配模块
import re

def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT='%a %b %d %H:%M:%S +0800 %Y'
    timeArray=datetime.datetime.strptime(v_str,GMT_FORMAT)
    ret_time=timeArray.strftime("%Y-%m-%d  %H:%M:%S")
    return  ret_time
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=1&feature=0
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=2&feature=0&since_id=4919182720239939kp2
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=3&feature=0&since_id=4915180460316608kp3
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=4&feature=0&since_id=4912678646582622kp4
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Cookie":"SINAGLOBAL=1863967907911.2815.1639802230789; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWO9cJpHbMEfRKRU2AaxlnC5JpX5KMhUgL.Foz71hzEeh5fSK22dJLoIp8KUgf_9PiW9rxLMJ4adc4kP7tt; UOR=,,login.sina.com.cn; ULV=1688778837811:26:4:3:5701773373218.957.1688778837628:1688282021181; XSRF-TOKEN=w4y_bOOr573M-oJ4TvpECz4s; ALF=1691482946; SSOLoginState=1688890955; SCF=Ak091LnJ-InHh8J_v9_Z53yWWQwHA8KDrVfSeuoa3I1E4N_ySgNThz83EIgAOxNSX__C8o3l9uBDVUoHiBpWAoQ.; SUB=_2A25Jrh4cDeRhGeRO41AT8C7Jzj2IHXVq2gjUrDV8PUNbmtANLUrRkW9NUEmRQE20K6K6rsAFf3iZmENTCeYxaEA0; WBPSESS=Kk15ov95J8WHQrCkca4auO5svOnPep0T7UplebD51dT0dugrZXimtQ-dTRBxBck1YzWn1vQvguc6WY5tBfS-V7qGP5DxVbxcaEWJxVPv3QNCSObhQuEhRuKA_fURzeUmymoQ1rRkW2Ge5Pwuss-plw==",
    "Referer":"https://weibo.com/n/%E5%B0%8F%E5%A8%B4%E4%B8%80%E7%B1%B3%E5%85%AB"
}
since_id=""
weibo_list=[]
create_time_list=[]
region_list=[]
comments_count_list=[]
reposts_count_list=[]    #转发次数
attitudes_count_list=[]  #点赞次数
for page in range(1,5):
    if page==1:
        url=f"https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page={page}&feature=0"
    else:
        url=f"https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page={page}&feature=0&since_id={since_id}"
    print(url)
    response=requests.get(url=url,headers=headers)
    print(response.text)
    print(response.status_code)
    since_id=response.json()["data"]["since_id"]
    print(since_id)
    data_list=response.json()["data"]["list"]
    for data in data_list:
        text_raw=data["text_raw"]
        replace_str=text_raw.replace(u'\u200b', '') #\u200b是不可见字符
        replace_str2=replace_str.replace("[doge]"," ").replace("\n"," ") #把表情符狗头替换成空格，把换行符替换成空格
        weibo_list.append(replace_str2)

        created_at=trans_time(data["created_at"])   #发布时间，微博时间需要进行转换成标准格式
        create_time_list.append(created_at)
        # print(data)
        try:
            region_name=data["region_name"].replace("发布于 ","") #发布地点  例如："发布于 上海"，转换成"上海”
            region_list.append(region_name)
        except:                                      #有些数据没有该key
            region_list.append(" ")

        comments_count=data["comments_count"]
        comments_count_list.append(comments_count)

        reposts_count=data["reposts_count"]   #转发次数
        reposts_count_list.append(reposts_count)

        attitudes_count=data["attitudes_count"]
        attitudes_count_list.append(attitudes_count)
    time.sleep(2)

#TODO 用来写入到本地csv文件中
v_result_file='table/01-爬取多页微博内容.csv'
if os.path.exists(v_result_file):
    header=None
else:
    header=["发布时间","发布地点",'微博内容',"转发次数","评论条数","点赞次数"]

#TODO 创建DataFram
c={
    "create_time":create_time_list,
    "region_name":region_list,
    "weibo_text":weibo_list,
    "reposts_count":reposts_count_list,
    "comments_count":comments_count_list,
    "attitudes_count":attitudes_count_list
}
df=pd.DataFrame(c)
# df.to_csv(v_result_file,encoding='utf_8_sig',mode="w+",index=False,header=header)

#charset=utf8不对，改成charset=utf8mb4
engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost:3306/python?charset=utf8mb4")

df.to_sql(name='xiaoxian_weibotext',con=engine,if_exists='replace',index=True)