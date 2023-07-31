import requests
from pprint import pprint
#正则匹配模块
import re

#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=1&feature=0
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=2&feature=0
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Cookie":"SINAGLOBAL=1863967907911.2815.1639802230789; UOR=,,www.baidu.com; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5gQ-M2KToaya3EcUC1rmQN; ULV=1684587455926:19:1:1:6629960112182.707.1684587455922:1682050457247; SUB=_2AkMT1Tybf8NxqwJRmfgSz23ibYp_ygrEieKlic1AJRMxHRl-yT9vqhw-tRB6OFUSdA4RRP8Oa1mYYGSwgC-GesdUCDzI; WBPSESS=yr8Ogb3qBlrorv2L6-ukSuBRCAR5n67nsIqDY2wEah28KdLTbMB6HAjBsr4ZVXpsmioJLN-h2aTHeX8kRqMkMbXneGY0j0JZt-uh1b-MEY0LyfQ67Tz-68NN2gYH7sJxZnmr0n2IDpNY-X4vrZE7dRHZFkDEnG-M_1kscMRePJA=; XSRF-TOKEN=DA2eAdw6VprSwvYk3HdjjIGJ",
    "Referer":"https://weibo.com/n/%E5%B0%8F%E5%A8%B4%E4%B8%80%E7%B1%B3%E5%85%AB"
}
url="https://weibo.com/ajax/statuses/mymblog?uid=2169289293&page=1&feature=0"
response=requests.get(url=url,headers=headers)
data_list=response.json()["data"]["list"]
one_pic_url=data_list[0]["pic_infos"]["814cba4dly1h65thtwshfj22tc480ao2"]["large"]["url"]
# one_pic_url=data_list[0]["pic_infos"]


pprint(type(one_pic_url))
one_pic_response=requests.get(url=one_pic_url,headers=headers).content
number=1
with open(f"img/{number}.jpg",mode="wb") as f:
    f.write(one_pic_response)
