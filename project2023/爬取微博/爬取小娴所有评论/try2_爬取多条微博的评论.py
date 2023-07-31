import  requests
import configparser      #配置文件解析模块
import tool              #工具类
import logging
import re                #正则匹配模块
import  pandas  as pd    #数据处理
import sqlalchemy        #mysql
import pymysql           #读取mysql的数据
import time
#https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4920602845253814&is_show_bulletin=2&is_mix=0&count=20&type=feed&uid=1306505563&fetch_level=0
#https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=4920602845253814&is_show_bulletin=2&is_mix=0&max_id=139281364595248&count=20&uid=1306505563&fetch_level=0
#https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=4920602845253814&is_show_bulletin=2&is_mix=0&max_id=139281297202544&count=20&uid=1306505563&fetch_level=0
from 爬取微博.爬取小娴所有评论.tool import trans_gender


class WeiboComment:
    def __init__(self,user_agent,cookie,referer):
        self.user_agent=user_agent
        self.cookie=cookie
        self.referer=referer
        self.url="https://weibo.com/ajax/statuses/buildComments"
        self.max_id=""
        self.page_list=[]
        self.id_list=[]
        self.text_list=[]
        self.time_list=[]
        self.like_count_list=[]      # 评论点赞数
        self.source_list=[]          # 评论者IP归属地
        self.user_name_list=[]       # 评论者姓名
        self.user_id_list=[]         # 评论者id
        self.user_gender_list=[]     # 评论者性别
        self.follow_count_list=[]    # 评论者关注数
        self.followers_count_list=[] # 评论者粉丝数

    def fetchUrl(self,weibo_id):
        for page in range(1,100):
            headers = {
                "User-Agent":self.user_agent,
                "Cookie":self.cookie,
                "Referer":self.referer
            }
            # 参数
            if(page == 1 ):
                params = {
                    "is_reload" : 1,
                    "id" : weibo_id,
                    "is_show_bulletin" : 2,
                    "is_mix" : 0,
                    "count" : 20,
                    "uid" : 1306505563,
                    "fetch_level":0
                }

            else:
                params = {
                    "flow":0,
                    "is_reload" : 1,
                    "id" : weibo_id,
                    "is_show_bulletin" : 2,
                    "is_mix" : 0,
                    "max_id":self.max_id,
                    "count" : 20,
                    "uid" : 1306505563,
                    "fetch_level":0
                }

            respnse = requests.get(self.url, headers = headers, params = params)
            logging.info(f"请求地址为：{respnse.url}")
            data_json=respnse.json()  #json格式
            logging.info(f"返回数据为{data_json}")
            self.max_id=data_json["max_id"]
            if(self.max_id==0):# 如果发现max_id为0，说明没有下一页了，break结束循环
                logging.info(f"当前微博id:{weibo_id}已加载完成!")
                break
            datas = data_json['data']
            for data in datas:
                self.page_list.append(page)
                self.id_list.append(data['id'])
                dr = re.compile(r'<[^>]+>', re.S)  # 用正则表达式清洗评论数据
                text2 = dr.sub('', data['text'])
                self.text_list.append(text2)  # 评论内容
                self.time_list.append(tool.trans_time(v_str=data['created_at']))  # 评论时间
                try :
                    like_count=data['like_counts']
                    self.like_count_list.append(like_count)  # 评论点赞数
                except:
                   self.like_count_list.append("")  # 评论点赞数

                try:
                    source=data['source'].repalce("来自","")
                    self.source_list.append(source)  # 评论者IP归属地
                except:
                    self.source_list.append("")

                try:
                    screen_name=data['user']['screen_name']
                    self.user_name_list.append(screen_name)  # 评论者姓名
                except:
                    self.user_name_list.append("")  # 评论者姓名

                try:
                    user_id=data['user']['id']
                    self.user_id_list.append(user_id)  # 评论者id
                except:
                    self.user_id_list.append("")

                try:
                    gender=data['user']['gender']
                    self.user_gender_list.append(trans_gender(data['user']['gender']))  # 评论者性别
                except:
                    self.user_gender_list.append("")

                try:
                    follow_count=data['user']['friends_count']
                    self.follow_count_list.append(follow_count)  # 评论者关注数
                except:
                    self.follow_count_list.append("")

                try:
                    followers_count=data['user']['followers_count']
                    self.followers_count_list.append(followers_count)  # 评论者粉丝数
                except:
                    self.followers_count_list.append("")

            deal_data={
                    '微博id': weibo_id,
                    '评论页码': self.page_list,
                    '评论id': self.id_list,
                    '评论时间': self.time_list,
                    '评论点赞数': self.like_count_list,
                    '评论者IP归属地': self.source_list,
                    '评论者姓名': self.user_name_list,
                    '评论者id': self.user_id_list,
                    '评论者性别': self.user_gender_list,
                    '评论者关注数': self.follow_count_list,
                    '评论者粉丝数': self.followers_count_list,
                    '评论内容': self.text_list
                }
        # print(deal_data)
        dataframe=pd.DataFrame(deal_data)
        return dataframe

#TODO 写入到mysql
def write_mysql(dataframe,bozhu):
    #charset=utf8不对，改成charset=utf8mb4
    engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost:3306/python?charset=utf8mb4")
    logging.info("写入到MySQL数据库开始")
    dataframe.to_sql(name=f'{bozhu}_weibo_comment',con=engine,if_exists='replace',index=True)
    logging.info("写入到MySQL数据库结束")

#TODO 读取mysql数据
def read_mysql_weibo_id():
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        db="python",
        charset="utf8"
    )  #获取连接

    cursor = conn.cursor()    #获取游标
    sql = """select weibo_id from xiaoxian_weibo_text group by weibo_id"""
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchall()
    # 处理结果为列表
    weibo_id_list = [result[0] for result in results]
    conn.commit()  #提交
    cursor.close()
    conn.close()
    print(weibo_id_list)
    return weibo_id_list

if __name__ == '__main__':
    tool.cache()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    # 创建一个ConfigParser对象
    config = configparser.ConfigParser()
    # 读取配置文件
    config.read('comment_config')
    # 获取配置文件中的值
    user_agent=config.get("headers_info","user-agent")
    cookie=config.get("headers_info","cookie")
    referer=config.get("headers_info","referer")
    bozhu="xiaoxian"
    weibo_comment=WeiboComment(user_agent,cookie,referer)
    for weibo_id in read_mysql_weibo_id():
        logging.info(f"weibo_id为{weibo_id}已开始请求")
        df=weibo_comment.fetchUrl(weibo_id)
        write_mysql(df,bozhu)
        logging.info(f"weibo_id为{weibo_id}已写入mysql")
        time.sleep(1)


