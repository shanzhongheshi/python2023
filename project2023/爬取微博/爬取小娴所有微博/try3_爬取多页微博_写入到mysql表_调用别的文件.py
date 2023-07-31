import requests
from pprint import pprint
import requests_cache  #缓存
import time   #请求完要睡眠
import  os #写入到文件
import pandas as pd
import datetime   #处理微博时间
import configparser  #读取配置文件
import sqlalchemy
import tool




#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=1&feature=0
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=2&feature=0&since_id=4919182720239939kp2
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=3&feature=0&since_id=4915180460316608kp3
#https://weibo.com/ajax/statuses/mymblog?uid=1306505563&page=4&feature=0&since_id=4912678646582622kp4

class WeiboText:
    def __init__(self,uid,cookie,referer):
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Cookie":cookie,
            "Referer":referer
        }
        self.uid=uid
        self.since_id=""
        self.weibo_list=[]            #微博内容
        self.create_time_list=[]      #发布时间
        self.region_list=[]           #发布地点
        self.comments_count_list=[]   #评论次数
        self.reposts_count_list=[]    #转发次数
        self.attitudes_count_list=[]  #点赞次数


    def get_data(self,start_page,end_page):
        for page in range(start_page,end_page):
            if page==1:
                url=f"https://weibo.com/ajax/statuses/mymblog?uid={self.uid}&page={page}&feature=0"
            else:
                url=f"https://weibo.com/ajax/statuses/mymblog?uid={self.uid}&page={page}&feature=0&since_id={since_id}"
            print(url)
            response=requests.get(url=url,headers=self.headers)
            print(response.text)
            print(response.status_code)
            since_id=response.json()["data"]["since_id"]
            print(since_id)
            data_list=response.json()["data"]["list"]
            for data in data_list:
                text_raw=data["text_raw"]
                replace_str=text_raw.replace(u'\u200b', '') #\u200b是不可见字符
                replace_str2=replace_str.replace("[doge]"," ").replace("\n"," ") #把表情符狗头替换成空格，把换行符替换成空格
                self.weibo_list.append(replace_str2)

                created_at=tool.trans_time(data["created_at"])   #发布时间，微博时间需要进行转换成标准格式
                self.create_time_list.append(created_at)
                # print(data)
                try:
                    region_name=data["region_name"].replace("发布于 ","") #发布地点  例如："发布于 上海"，转换成"上海”
                    self.region_list.append(region_name)
                except:                                      #有些数据没有该key
                    self.region_list.append(" ")

                comments_count=data["comments_count"]
                self.comments_count_list.append(comments_count)

                reposts_count=data["reposts_count"]   #转发次数
                self.reposts_count_list.append(reposts_count)

                attitudes_count=data["attitudes_count"]
                self.attitudes_count_list.append(attitudes_count)
            time.sleep(2)

        data_list_json={
            "create_time":self.create_time_list,
            "region_name":self.region_list,
            "weibo_text":self.weibo_list,
            "reposts_count":self.reposts_count_list,
            "comments_count":self.comments_count_list,
            "attitudes_count":self.attitudes_count_list
        }
        return data_list_json


#TODO 创建DataFram
def create_datafame(data_list_json):
    df=pd.DataFrame(data_list_json)
    return df


#TODO 用来写入到本地csv文件中
def write_csv(csv_fiel_name,dataframe):
    v_result_file=f'table/{csv_fiel_name}.csv'
    # v_result_file='table/01-爬取多页微博内容.csv'
    if os.path.exists(v_result_file):
        header=None
    else:
        header=["发布时间","发布地点",'微博内容',"转发次数","评论条数","点赞次数"]
    dataframe.to_csv(v_result_file,encoding='utf_8_sig',mode="w+",index=False,header=header)

#TODO 写入到mysql
def write_mysql(dataframe,bozhu):
    #charset=utf8不对，改成charset=utf8mb4
    engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost:3306/python?charset=utf8mb4")
    dataframe.to_sql(name=f'{bozhu}_weibotext',con=engine,if_exists='replace',index=True)

if __name__ == '__main__':
    bozhu_str = input("请输入您要查看的博主：");
    # 创建一个ConfigParser对象
    config = configparser.ConfigParser()

    # 读取配置文件
    config.read('config')

    # 获取配置文件中的值
    uid = config.get(bozhu_str, 'uid')
    csv_file_name=config.get(bozhu_str, 'csv_file_name')
    print(uid,csv_file_name)
    tool.cache()
    cookie=config.get("headers_info","cookie")
    referer=config.get("headers_info","referer")
    weibo=WeiboText(uid,cookie,referer)
    data=weibo.get_data(1,10)
    df=create_datafame(data)
    write_mysql(df,bozhu_str)