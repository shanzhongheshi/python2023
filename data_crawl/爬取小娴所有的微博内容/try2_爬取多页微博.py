import requests
from pprint import pprint
#正则匹配模块
import re

#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=1&feature=0
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=2&feature=0
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Cookie":"SINAGLOBAL=1863967907911.2815.1639802230789; UOR=,,www.baidu.com; XSRF-TOKEN=DA2eAdw6VprSwvYk3HdjjIGJ; PC_TOKEN=7c7ab67d89; login_sid_t=acbcc90c426aa66e58041baf6fd4ad46; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; wb_view_log=1536*8641.25; _s_tentry=weibo.com; Apache=6109188491998.778.1687576997000; ULV=1687576997008:20:1:1:6109188491998.778.1687576997000:1684587455926; SSOLoginState=1687577064; SUB=_2A25JkhG4DeRhGeRO41AT8C7Jzj2IHXVq5gRwrDV8PUNbmtANLXXmkW9NUEmRQAXgKVgLQ4oHrvLxQhCQTIEglqEk; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWO9cJpHbMEfRKRU2AaxlnC5JpX5KzhUgL.Foz71hzEeh5fSK22dJLoIp8KUgf_9PiW9rxLMJ4adc4kP7tt; ALF=1719113063; WBPSESS=Kk15ov95J8WHQrCkca4auO5svOnPep0T7UplebD51dStGTf4zOTWw7d3zm86TedU_OdEtLfhqocHovJHA8aGZx1zco1wiT18CLbddTMIMyD6sSKXvFpo3UKhXtDTpwsll5qw7dTyiqWhy4gV9tiOPw==",
    "Referer":"https://weibo.com/n/%E5%B0%8F%E5%A8%B4%E4%B8%80%E7%B1%B3%E5%85%AB"
}
for page in range(1,11):
    url=f"https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page={page}&feature=0"
    response=requests.get(url=url,headers=headers)
    data_list=response.json()["data"]["list"]
    for data in data_list:
        text_raw=data["text_raw"]
        re_text=''.join(re.findall('[(\u4e00-\u9fa5)(0-9)(.，。（）【】{}！,!)(\\-)]+',text_raw))
        print(re_text)