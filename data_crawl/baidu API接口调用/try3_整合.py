import requests
import json
from pprint import pprint
import pandas as pd
import os


def get_token():

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=l7P4YUZ2GRO8LPiwK2SM7aOn&client_secret=klcTBfcwXbSmFeGLmohU7E70WRdWcKR5"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    access_token=response.json()["access_token"]
    return access_token

def sentiment_analyse(access_token,charset,text):

    url = f"https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token={access_token}&charset={charset}"
    payload = json.dumps({"text":f"{text}"})
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    sentiment_dict=response.json()
    return sentiment_dict
    print(type(sentiment_dict))

if __name__ == '__main__':
    text_list=['今天天气不错','没睡好']
    access_token=get_token()
    charset='UTF-8'
    confidence_list=[]
    neg_list=[]
    pos_list=[]
    tag_list=[]
    for text in text_list:
        sentiment_dict=sentiment_analyse(access_token,charset,text)
        print(sentiment_dict)
        confidence_list.append(sentiment_dict["items"][0]["confidence"])
        neg_list.append(sentiment_dict["items"][0]["negative_prob"])
        pos=sentiment_dict["items"][0]["positive_prob"]
        pos_list.append(pos)
        if pos<0.5:
            tag='消极'
        elif pos>0.5:
            tag="积极"
        else:
            tag="中性"
        tag_list.append(tag)

    v_result_file='百度情感分析.csv'
    if os.path.exists(v_result_file):
        header=None
    else:
        header=['文本内容','置信度','消极概率','积极概率','分析结果']

    c={"文本内容":text_list,
       "置信度":confidence_list,
       "消极概率":neg_list,
       "积极概率":pos_list,
       "分析结果":tag_list
       }
    df=pd.DataFrame(c)
    # df.to_csv(v_result_file,encoding='utf_8_sig',mode="a+",index=False,header=header)
    print(df)


