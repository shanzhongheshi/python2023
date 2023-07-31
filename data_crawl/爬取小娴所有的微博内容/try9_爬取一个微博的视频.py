import  requests


# url="https://video.weibo.com/show?fid=1034:4915107445276702&mark_id=999_reallog_mark_ad%3A999%7CWeiboADNatural"
url="https://f.video.weibocdn.com/o0/UR9hyDSslx086pxuziCs0104120aQwsy0E040.mp4?label=mp4_720p&template=1280x720.25.0&media_id=4915107445276702&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=2&ot=h&lp=16059ZhHAJWY5qSJ5WuSZy&ps=mZ6WB&uid=2gUHtR&ab=11243-g2,3601-g32,8143-g0,8013-g0,7598-g0&Expires=1687618194&ssig=ePdmWexfUv&KID=unistore,video"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Cookie":"SINAGLOBAL=1863967907911.2815.1639802230789; UOR=,,www.baidu.com; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5gQ-M2KToaya3EcUC1rmQN; ULV=1684587455926:19:1:1:6629960112182.707.1684587455922:1682050457247; SUB=_2AkMT1Tybf8NxqwJRmfgSz23ibYp_ygrEieKlic1AJRMxHRl-yT9vqhw-tRB6OFUSdA4RRP8Oa1mYYGSwgC-GesdUCDzI; WBPSESS=yr8Ogb3qBlrorv2L6-ukSuBRCAR5n67nsIqDY2wEah28KdLTbMB6HAjBsr4ZVXpsmioJLN-h2aTHeX8kRqMkMbXneGY0j0JZt-uh1b-MEY0LyfQ67Tz-68NN2gYH7sJxZnmr0n2IDpNY-X4vrZE7dRHZFkDEnG-M_1kscMRePJA=; XSRF-TOKEN=DA2eAdw6VprSwvYk3HdjjIGJ",
    "Referer":"https://weibo.com/n/%E5%B0%8F%E5%A8%B4%E4%B8%80%E7%B1%B3%E5%85%AB"
}
response=requests.get(url=url,headers=headers).content

with open(f"video/1.mp4",mode="wb") as f:
    f.write(response)