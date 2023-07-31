import pprint
import re
import  requests
import csv
import  pandas as pd
url='https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4874485926200475&is_show_bulletin=2&is_mix=0&count=10&uid=1192966660'
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'cookie': 'SCF=AlyYCUTSNP67WvyClzxK7WVOYg-I3xwX71ESRR4UjTPCs1uIUlmcSar0ejHylYBYcbFbWkxfV_XejOlVOu4WtLo.; UOR=,,www.baidu.com; SINAGLOBAL=1863967907911.2815.1639802230789; SUB=_2AkMUp5zkf8NxqwJRmfgSz23ibYp_ygrEieKi-20_JRMxHRl-yj9kqlYdtRB6PyeyC7CM8Y2R3zJKZAPUI_ICSSorElc0; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5gQ-M2KToaya3EcUC1rmQN; XSRF-TOKEN=H5qca-YcTmgKsVxVvp4YnHpO; _s_tentry=www.weibo.com; Apache=3966038964329.981.1677677192146; ULV=1677677192178:17:1:4:3966038964329.981.1677677192146:1677399180510; WBPSESS=yr8Ogb3qBlrorv2L6-ukSuBRCAR5n67nsIqDY2wEah28KdLTbMB6HAjBsr4ZVXpsl-04V8DSLAt4DyZ9RUHviX63zRO_ZZGpSrWUKeMd9G0SHazvmRHA0kGNJ-cpNm3YHttmCArez8errolE_QoVX6uV25_9TjsJ4lsN-VqY2XQ='
}
response=requests.get(url=url,headers=header)
#print(response.json())
#TODO 打印一条数据
def test1():
    for index in response.json()['data']:
        content=''.join(re.findall('[(\u4e00-\u9fa5)(，。（）【】{}！,!)]+',index['text']))
        pprint.pprint(content)


if __name__ == '__main__':
  test1()
