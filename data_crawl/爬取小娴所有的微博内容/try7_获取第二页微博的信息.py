import requests
from pprint import pprint
#正则匹配模块
import re

#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=1&feature=0
#https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page=2&feature=0&since_id=4343195246366414kp2
#https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page=3&feature=0&since_id=4237567777651754kp3
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",
    "Cookie":"SINAGLOBAL=1863967907911.2815.1639802230789; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWO9cJpHbMEfRKRU2AaxlnC5JpX5KMhUgL.Foz71hzEeh5fSK22dJLoIp8KUgf_9PiW9rxLMJ4adc4kP7tt; XSRF-TOKEN=o4T1sZ4xrndjTGSnYxyDVzJ0; ALF=1690165577; SSOLoginState=1687573577; SCF=AlyYCUTSNP67WvyClzxK7WVOYg-I3xwX71ESRR4UjTPCykjYfDk0zOf0JZY9EuONpB5gxXPMMKrQtptkPFVthJo.; SUB=_2A25JkiQaDeRhGeRO41AT8C7Jzj2IHXVq5hLSrDV8PUNbmtANLRjVkW9NUEmRQFv_88I3gKfVqnc3kotjGJ5sOgdk; WBPSESS=Kk15ov95J8WHQrCkca4auO5svOnPep0T7UplebD51dStGTf4zOTWw7d3zm86TedU_OdEtLfhqocHovJHA8aGZ5cCuvLLxY2o2V0qPRvZp8EVTj0_FijSSRT4SLFwYSNGHKrq0oCIr4cRq9p-5KwDvA==; _s_tentry=-; Apache=5087122242554.023.1687575773474; ULV=1687575773554:24:6:3:5087122242554.023.1687575773474:1687482181673",
    "Referer":"https://weibo.com/u/2169289293"
}
since_id=""
number=1
for page_id in range (1,6):
    if page_id==1:
        url=f"https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page={page_id}&feature=0"
    else:
        url=f"https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page={page_id}&feature=0&since_id={since_id}"
    print(url)
    response=requests.get(url=url,headers=headers)
    data_json=response.json()["data"]
    data_list=data_json["list"]
    since_id=data_json["since_id"]
    for data in data_list:
        try:
            one_weibo_pic_infos_data=data["pic_infos"] #一个微博的所有图片信息，是字典类型
        except:
            print()
        else:
            for one_pic_info in one_weibo_pic_infos_data:
                one_pic_url=one_weibo_pic_infos_data[one_pic_info]["large"]["url"]
                one_pic_response=requests.get(url=one_pic_url,headers=headers).content

                with open(f"img/{number}.jpg",mode="wb") as f:
                    f.write(one_pic_response)
                number+=1

