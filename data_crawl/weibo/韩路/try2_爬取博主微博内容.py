import pprint
import re
import  requests
import csv
import  pandas as pd
url='https://m.weibo.cn/comments/hotflow?id=4873379708932041&mid=4873379708932041&max_id_type=0'
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response=requests.get(url=url,headers=header)
#print(response.json())
#TODO 打印一条数据
def test1():
    for index in response.json()['data']['data']:
        pprint.pprint(index)
        break

def test2():
    for index in response.json()['data']['data']:
        # content=''.join(re.findall('[\u4e00-\u9fa5]+|[a-zA-Z]+',index['text']))
        # content=''.join(re.findall('[(\u4e00-\u9fa5)(A-Za-z0-9)(，。（）【】{}！,.\-!)]+',index['text']))
        content=''.join(re.findall('[(\u4e00-\u9fa5)(，。（）【】{}！,!)]+',index['text']))

        dit={
            '用户':index['user']['screen_name'],
            '地区':index['source'].replace('来自',''),
            '评论':content,
            '日期':index['created_at']
        }
        print(dit)
#TODO 写入csv文件
def test3():
    lit=[]
    f=open('tmp/微博评论.csv',mode='a',encoding='utf-8',newline='')
    #写入字段名
    csv_writer=csv.DictWriter(f,fieldnames=[
        '用户',
        '地区',
        '评论',
        '日期'
    ])
    csv_writer.writeheader() #写入表头
    for index in response.json()['data']['data']:
        # content=''.join(re.findall('[\u4e00-\u9fa5]+|[a-zA-Z]+',index['text']))
        # content=''.join(re.findall('[(\u4e00-\u9fa5)(A-Za-z0-9)(，。（）【】{}！,.\-!)]+',index['text']))
        content=''.join(re.findall('[(\u4e00-\u9fa5)(，。（）【】{}！,!)]+',index['text']))

        dit={
            '用户':index['user']['screen_name'],
            '地区':index['source'].replace('来自',''),
            '评论':content,
            '日期':index['created_at']
        }
        lit.append(dit)
        csv_writer.writerow(dit)
#TODO 写入excel文件
def test4():
    lit=[]
    for index in response.json()['data']['data']:
        # content=''.join(re.findall('[\u4e00-\u9fa5]+|[a-zA-Z]+',index['text']))
        # content=''.join(re.findall('[(\u4e00-\u9fa5)(A-Za-z0-9)(，。（）【】{}！,.\-!)]+',index['text']))
        content=''.join(re.findall('[(\u4e00-\u9fa5)(，。（）【】{}！,!)]+',index['text']))

        dit={
            '用户':index['user']['screen_name'],
            '地区':index['source'].replace('来自',''),
            '评论':content,
            '日期':index['created_at']
        }
        lit.append(dit)
    pd_data=pd.DataFrame(lit)
    pd_data.to_excel('微博评论.xlsx')

if __name__ == '__main__':
  # test1()
  # test2()
  # test3()
  test4()