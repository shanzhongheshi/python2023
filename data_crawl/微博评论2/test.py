import requests
url="https://www.weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=4912454217237229&is_show_bulletin=2&is_mix=0&max_id=141067452938524&count=20&uid=1192966660&fetch_level=0"

# 请求头
# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",
    "cookie":"SINAGLOBAL=1863967907911.2815.1639802230789; XSRF-TOKEN=WgwNYrUMFxdiG-785p7y_jMu; PC_TOKEN=0d7d8f508a; login_sid_t=07fc874c281b9f4466ffdab2c9884050; cross_origin_proto=SSL; _s_tentry=www.weibo.com; Apache=9442571091209.996.1686748882656; ULV=1686748882660:21:3:1:9442571091209.996.1686748882656:1685624282092; SSOLoginState=1686748933; SCF=AlyYCUTSNP67WvyClzxK7WVOYg-I3xwX71ESRR4UjTPC1Gtbq9V-t3zyxoxolghRmZU4FfBnMat6hRJa9VudNfE.; SUB=_2A25Jjc9VDeRhGeRO41AT8C7Jzj2IHXVq-qedrDV8PUNbmtAGLVDlkW9NUEmRQJ5DmNcELwI2CsPEu_BUz7PtB_mq; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWO9cJpHbMEfRKRU2AaxlnC5JpX5KzhUgL.Foz71hzEeh5fSK22dJLoIp8KUgf_9PiW9rxLMJ4adc4kP7tt; ALF=1718284932; WBPSESS=Kk15ov95J8WHQrCkca4auO5svOnPep0T7UplebD51dStGTf4zOTWw7d3zm86TedUHWC5OO_2eBeqmHkww7BeKcvFkF-JrB7eVxX3QICR8LL30EZgUxAsLjHmNvumUHVu6L5Cz9kR295eJmDqVcVrkw==referer: https://www.weibo.com/1192966660/N5dZrumJv"
}
r=requests.get(url,headers)
print(r.status_code)