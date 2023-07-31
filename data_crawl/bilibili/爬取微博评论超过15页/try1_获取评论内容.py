import  requests
import re
import  pandas as pd

#分析
#https://m.weibo.cn/comments/hotflow?id=4907928123605557&mid=4907928123605557&max_id_type=0
#https://m.weibo.cn/comments/hotflow?id=4907928123605557&mid=4907928123605557&max_id=142853879476142&max_id_type=0
#https://m.weibo.cn/comments/hotflow?id=4907928123605557&mid=4907928123605557&max_id=140242539793114&max_id_type=0
#
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
}
weibo_id='4907928123605557'
max_id=''
page=1
page_list=[]
id_list=[]
text_list=[]
time_list=[]
like_count_list=[]
source_list=[]
user_name_list=[]
user_id_list=[]
user_gender_list=[]
follow_count_list=[]
followers_count_list=[]
while 1==1:
    if page == 1:  # 第一页，没有max_id参数
        url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0'.format(weibo_id, weibo_id)
    else:  # 非第一页，需要max_id参数
        if max_id == '0':  # 如果发现max_id为0，说明没有下一页了，break结束循环
            print('max_id is 0, break now')
            break
        url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type=0'.format(weibo_id,weibo_id,max_id)
        print(url)
    r=requests.get(url,headers=headers)
    r.encoding=r.apparent_encoding
    page += 1
    text=r.json()
    print(text)
    max_id=text["data"]["max_id"]
    print(max_id)
#     datas = r.json()['data']['data']

#     for data in datas:
#         page_list.append(page)
#         id_list.append(data['id'])
#         dr = re.compile(r'<[^>]+>', re.S)  # 用正则表达式清洗评论数据
#         text2 = dr.sub('', data['text'])
#         text_list.append(text2)  # 评论内容
#         time_list.append(data['created_at']) # 评论时间
#         like_count_list.append(data['like_count'])  # 评论点赞数
#         source_list.append(data['source'])  # 评论者IP归属地
#         user_name_list.append(data['user']['screen_name'])  # 评论者姓名
#         user_id_list.append(data['user']['id'])  # 评论者id
#         user_gender_list.append(data['user']['gender'])  # 评论者性别
#         follow_count_list.append(data['user']['follow_count'])  # 评论者关注数
#         followers_count_list.append(data['user']['followers_count'])  # 评论者粉丝数
#
# df = pd.DataFrame(
#     {
#         '微博id': [weibo_id] * len(time_list),
#         '评论页码': page_list,
#         '评论id': id_list,
#         '评论时间': time_list,
#         '评论点赞数': like_count_list,
#         '评论者IP归属地': source_list,
#         '评论者姓名': user_name_list,
#         '评论者id': user_id_list,
#         '评论者性别': user_gender_list,
#         '评论者关注数': follow_count_list,
#         '评论者粉丝数': followers_count_list,
#         '评论内容': text_list,
#     }
# )