import requests
from pprint import pprint
#正则匹配模块
import re

#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=1&feature=0
#https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page=2&feature=0&since_id=4343195246366414kp2
#https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page=3&feature=0&since_id=4237567777651754kp3
class Xinlangweibo:
    def __init__(self):
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Cookie":"SINAGLOBAL=1863967907911.2815.1639802230789; UOR=,,www.baidu.com; XSRF-TOKEN=DA2eAdw6VprSwvYk3HdjjIGJ; PC_TOKEN=7c7ab67d89; login_sid_t=acbcc90c426aa66e58041baf6fd4ad46; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; wb_view_log=1536*8641.25; _s_tentry=weibo.com; Apache=6109188491998.778.1687576997000; ULV=1687576997008:20:1:1:6109188491998.778.1687576997000:1684587455926; SSOLoginState=1687577064; SUB=_2A25JkhG4DeRhGeRO41AT8C7Jzj2IHXVq5gRwrDV8PUNbmtANLXXmkW9NUEmRQAXgKVgLQ4oHrvLxQhCQTIEglqEk; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWO9cJpHbMEfRKRU2AaxlnC5JpX5KzhUgL.Foz71hzEeh5fSK22dJLoIp8KUgf_9PiW9rxLMJ4adc4kP7tt; ALF=1719113063; WBPSESS=Kk15ov95J8WHQrCkca4auO5svOnPep0T7UplebD51dStGTf4zOTWw7d3zm86TedU_OdEtLfhqocHovJHA8aGZx1zco1wiT18CLbddTMIMyD6sSKXvFpo3UKhXtDTpwsll5qw7dTyiqWhy4gV9tiOPw==",
            "Referer":"https://weibo.com/n/%E5%B0%8F%E5%A8%B4%E4%B8%80%E7%B1%B3%E5%85%AB"
        }
        self.since_id=""
        self.number=1


    def get_pics(self,start_page,end_page):
        for page_id in range (start_page,end_page):
            if page_id==1:
                url=f"https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page={page_id}&feature=0"
            else:
                url=f"https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page={page_id}&feature=0&since_id={since_id}"
            print(url)
            response=requests.get(url=url,headers=self.headers)
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
                        one_pic_response=requests.get(url=one_pic_url,headers=self.headers).content  #根据图片url请求

                        with open(f"img2/{self.number}.jpg",mode="wb") as f: #保存图片
                            f.write(one_pic_response)
                        self.number +=1

if __name__ == '__main__':
    weibo=Xinlangweibo()
    weibo.get_pics(1,10)

