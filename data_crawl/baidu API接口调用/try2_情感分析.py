import requests
import json
from pprint import pprint


def main():

    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=24.0a3c03ad35b54f779a6fdfbb8a6b47af.2592000.1689251436.282335-34686237&charset=UTF-8"
    # url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=25.d9ec654372dabfd59a13aab75154297d.315360000.2001850781.282335-34686237&charset=UTF-8"

    #将python对象编码成Json字符串
    payload = json.dumps({"text":""})
    print(type(payload))
    print(payload)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    pprint(response.text)


if __name__ == '__main__':
    main()
"""
{
"text": "曼联获得了欧冠冠军！",
"items": [
{
"confidence": 0.971878,
"negative_prob": 0.012655,
"positive_prob": 0.987345,
"sentiment": 2
}
],
"log_id": 1668597388645947924
}
"""

"""
log_id	uint64	请求唯一标识码
sentiment	int	表示情感极性分类结果，0:负向，1:中性，2:正向
confidence	float	表示分类的置信度，取值范围[0,1]
positive_prob	float	表示属于积极类别的概率 ，取值范围[0,1]
negative_prob	float	表示属于消极类别的概率，取值范围[0,1]
"""