import requests
from pprint import pprint
#正则匹配模块
import re

#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=1&feature=0
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=2&feature=0
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Cookie":"SINAGLOBAL=1863967907911.2815.1639802230789; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWO9cJpHbMEfRKRU2AaxlnC5JpX5KMhUgL.Foz71hzEeh5fSK22dJLoIp8KUgf_9PiW9rxLMJ4adc4kP7tt; UOR=,,login.sina.com.cn; ULV=1688778837811:26:4:3:5701773373218.957.1688778837628:1688282021181; XSRF-TOKEN=w4y_bOOr573M-oJ4TvpECz4s; ALF=1691482946; SSOLoginState=1688890955; SCF=Ak091LnJ-InHh8J_v9_Z53yWWQwHA8KDrVfSeuoa3I1E4N_ySgNThz83EIgAOxNSX__C8o3l9uBDVUoHiBpWAoQ.; SUB=_2A25Jrh4cDeRhGeRO41AT8C7Jzj2IHXVq2gjUrDV8PUNbmtANLUrRkW9NUEmRQE20K6K6rsAFf3iZmENTCeYxaEA0; WBPSESS=Kk15ov95J8WHQrCkca4auO5svOnPep0T7UplebD51dT0dugrZXimtQ-dTRBxBck1YzWn1vQvguc6WY5tBfS-V7qGP5DxVbxcaEWJxVPv3QNCSObhQuEhRuKA_fURzeUmymoQ1rRkW2Ge5Pwuss-plw==",
    "Referer":"https://weibo.com/n/%E5%B0%8F%E5%A8%B4%E4%B8%80%E7%B1%B3%E5%85%AB"
}
url="https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=3&feature=0"
# url="https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=3&feature=0&since_id=4915180460316608kp3"
response=requests.get(url=url,headers=headers)
print(response.text)  #字典类型
data_list=response.json()["data"]["list"]
# pprint(response.json()["data"]["list"][0]["text_raw"])
for data in data_list:
    text_raw=data["text_raw"]
    # re_text=''.join(re.findall('[(\u4e00-\u9fa5)(0-9)(.，。（）【】{}！,!)(\\-)]+',text_raw))  #使用正则替换，不是很理想，
    # print(re_text)
    replace_str=text_raw.replace(u'\u200b', '') #\u200b是不可见字符
    replace_str2=replace_str.replace("[doge]"," ").replace("\n"," ") #把表情符狗头替换成空格，把换行符替换成空格
    print(replace_str2)
    region_name=data["region_name"]  #发布地点
    print(region_name)


requests.po