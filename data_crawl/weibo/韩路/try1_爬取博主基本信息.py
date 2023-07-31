import requests
import re

def get_custom_info():
    url="https://weibo.com/ajax/profile/info?custom=NYLONCHINA"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "accept":"pplication/json, text/plain, */*",
        "accept-encoding":"gzip, deflate, br",
        "cookie": "SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5gQ-M2KToaya3EcUC1rmQN; SINAGLOBAL=1863967907911.2815.1639802230789; UOR=,,www.baidu.com; SUB=_2AkMUfdGef8NxqwJRmfgSz23ibYp_ygrEieKiISBFJRMxHRl-yT9jqhUutRB6P_3_cdCZkb-SWBho8pTfWZScYbdNQ6rL; XSRF-TOKEN=0ZJICGzdrMCOj_VZoH6jGDXN; _s_tentry=weibo.com; Apache=282205080632.2562.1665136554310; ULV=1665136554315:10:2:2:282205080632.2562.1665136554310:1665133471967; WBPSESS=yr8Ogb3qBlrorv2L6-ukSuBRCAR5n67nsIqDY2wEah28KdLTbMB6HAjBsr4ZVXpsntsZuv8KzdKllkzwdZZO4Zm3R2OqCEQx39jZpX2Z6BLsSbp4HV2-idRPpUddFUtXGH7rJBHP0vg9Gs6tlZIoV1YHDdgOlCoQ-ADFG23ULb0="
    }

    response = requests.get(url=url, headers=headers)

    context=response.json()  #context是字典
    id = context["data"]["user"]["id"]  #获取id
    followers_counts = context["data"]["user"]["followers_count"]  #获取粉丝量
    friends_count = context["data"]["user"]["friends_count"]   #获取好友数量
    verified_reason = context["data"]["user"]["verified_reason"] #获取名称
    print(id,followers_counts,friends_count,verified_reason)

def get_url_text():

    url='https://weibo.com/ajax/statuses/mymblog?uid=6298663816&page=1&feature=0'
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "accept":"pplication/json, text/plain, */*",
        "accept-encoding":"gzip, deflate, br",
        "cookie": "SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5gQ-M2KToaya3EcUC1rmQN; SINAGLOBAL=1863967907911.2815.1639802230789; UOR=,,www.baidu.com; SUB=_2AkMUfdGef8NxqwJRmfgSz23ibYp_ygrEieKiISBFJRMxHRl-yT9jqhUutRB6P_3_cdCZkb-SWBho8pTfWZScYbdNQ6rL; XSRF-TOKEN=0ZJICGzdrMCOj_VZoH6jGDXN; _s_tentry=weibo.com; Apache=282205080632.2562.1665136554310; ULV=1665136554315:10:2:2:282205080632.2562.1665136554310:1665133471967; WBPSESS=yr8Ogb3qBlrorv2L6-ukSuBRCAR5n67nsIqDY2wEah28KdLTbMB6HAjBsr4ZVXpsntsZuv8KzdKllkzwdZZO4Zm3R2OqCEQx39jZpX2Z6BLsSbp4HV2-idRPpUddFUtXGH7rJBHP0vg9Gs6tlZIoV1YHDdgOlCoQ-ADFG23ULb0="
    }

    response = requests.get(url=url, headers=headers)

    context=response.json()
    text_raw = context["data"]["list"][2]["text_raw"]

    dr=re.compile(r'<[^>]+>',re.S)
    for text in text_raw:
        tq_text = dr.sub('', text)
        print(tq_text)


if __name__ == '__main__':
    # get_custom_info()
    get_url_text()
