# https://m.weibo.cn/comments/hotflow?id=4885831775166181&mid=4885831775166181&max_id_type=0
import requests
import re

def get_custom_info():
    url="https://m.weibo.cn/comments/hotflow?id=4885699427306962&mid=4885699427306962&max_id_type=3"
    # url="https://m.weibo.cn/comments/hotflow?id=4885699427306962&mid=4885699427306962&max_id=138866801957933&max_id_type=0"

    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "accept":"pplication/json, text/plain, */*",
        "accept-encoding":"gzip, deflate, br",
        "cookie": "SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5gQ-M2KToaya3EcUC1rmQN; SINAGLOBAL=1863967907911.2815.1639802230789; UOR=,,www.baidu.com; SUB=_2AkMUfdGef8NxqwJRmfgSz23ibYp_ygrEieKiISBFJRMxHRl-yT9jqhUutRB6P_3_cdCZkb-SWBho8pTfWZScYbdNQ6rL; XSRF-TOKEN=0ZJICGzdrMCOj_VZoH6jGDXN; _s_tentry=weibo.com; Apache=282205080632.2562.1665136554310; ULV=1665136554315:10:2:2:282205080632.2562.1665136554310:1665133471967; WBPSESS=yr8Ogb3qBlrorv2L6-ukSuBRCAR5n67nsIqDY2wEah28KdLTbMB6HAjBsr4ZVXpsntsZuv8KzdKllkzwdZZO4Zm3R2OqCEQx39jZpX2Z6BLsSbp4HV2-idRPpUddFUtXGH7rJBHP0vg9Gs6tlZIoV1YHDdgOlCoQ-ADFG23ULb0="
    }

    response = requests.get(url=url, headers=headers)

    context=response.json()  #context是字典
    comments = context["data"]["data"]
    for comment in comments:
        comment_text=comment['text']
        re_comment=''.join(re.findall('[(\u4e00-\u9fa5)(，。（）【】{}！,!)]+',comment_text))
        print(re_comment)


# https://m.weibo.cn/comments/hotflow?id=4885699427306962&mid=4885699427306962&max_id_type=0
# https://m.weibo.cn/comments/hotflow?id=4885699427306962&mid=4885699427306962&max_id=138866801957933&max_id_type=0
# https://m.weibo.cn/comments/hotflow?id=4885699427306962&mid=4885699427306962&max_id=138866793053638&max_id_type=0
# https://m.weibo.cn/comments/hotflow?id=4885699427306962&mid=4885699427306962&max_id=190891430717&max_id_type=0


if __name__ == '__main__':
    get_custom_info()
