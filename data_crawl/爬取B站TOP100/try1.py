import requests
import  pandas as pd
import os
url_dict = {
    '全站': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all',
    # '番剧': 'https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=1',  #
    # '国产动画': 'https://api.bilibili.com/pgc/season/rank/web/list?day=3&season_type=4',  #
    # '国创相关': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=168&type=all',  #
    # '纪录片': 'https://api.bilibili.com/pgc/season/rank/web/list?day=3&season_type=3',  #
    '动画': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=1&type=all',
    '音乐': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=3&type=all',
    '舞蹈': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=129&type=all',
    '游戏': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=4&type=all',
    '知识': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=36&type=all',
    '科技': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=188&type=all',
    '运动': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=234&type=all',
    '汽车': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=223&type=all',
    '生活': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=160&type=all',
    '美食': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=211&type=all',
    '动物圈': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=217&type=all',
    '鬼畜': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=119&type=all',
    '时尚': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=155&type=all',
    '娱乐': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=5&type=all',
    '影视': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=181&type=all',
    # # '电影': 'https://api.bilibili.com/pgc/season/rank/web/list?day=3&season_type=2',  #
    # # '电视剧': 'https://api.bilibili.com/pgc/season/rank/web/list?day=3&season_type=5',  #
    '原创': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=origin',
    '新人': 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=rookie',
}

url=url_dict["科技"]
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
r = requests.get(url, headers=headers)
print(r.status_code)
json_data = r.json()
list_data = json_data['data']['list']
title_list=[]
play_cnt_list=[]
danmu_cnt_list=[]
coin_cnt_list=[]
like_cnt_list=[]
share_cnt_list=[]
dislike_cnt_list=[]
favorite_cnt_list=[]
author_list=[]
score_list=[]
video_url=[]
for data in list_data:
    title_list.append(data['title'])  # 视频标题
    play_cnt_list.append(data['stat']['view'])  # 播放数
    danmu_cnt_list.append(data['stat']['danmaku'])  # 弹幕数
    coin_cnt_list.append(data['stat']['coin'])  # 投币数
    like_cnt_list.append(data['stat']['like'])  # 点赞数
    dislike_cnt_list.append(data['stat']['dislike'])  # 点踩数
    share_cnt_list.append(data['stat']['share'])  # 分享数
    favorite_cnt_list.append(data['stat']['favorite'])  # 收藏数
    author_list.append(data['owner']['name'])  # 作者
    score_list.append(data['score'])  # 评分
    video_url.append('https://www.bilibili.com/video/' + data['bvid'])  # 视频链接


v_result_file='科技.csv'
if os.path.exists(v_result_file):
    header=None
else:
    header=['视频标题','播放数','弹幕数','投币数','点赞数','点踩数','分享数','收藏数','作者','评分','视频链接']

c={"视频标题":title_list,
   "播放数":play_cnt_list,
   "弹幕数":danmu_cnt_list,
   "投币数":coin_cnt_list,
   "点赞数":like_cnt_list,
   "点踩数":dislike_cnt_list,
   "分享数":share_cnt_list,
   "收藏数":favorite_cnt_list,
   "作者":author_list,
   "评分":score_list,
   "视频链接":video_url
   }
df=pd.DataFrame(c)
print(df)