import requests
import json

# 视频的av号，可以在Bilibili网站上找到
av_id = "BV19P411Z78V"

page=1

# 评论API接口URL
url = f"https://api.bilibili.com/x/v2/reply?&type=1&oid={av_id}&pn={page}&sort=0"

# 获取前20页评论
for page in range(1, 21):
    # 发送请求并获取响应
    response = requests.get(url.format(page))
    # 将响应转换为json格式
    comments_json = json.loads(response.text)
    # 获取评论列表
    comments_list = comments_json["data"]["replies"]
    # 打印每条评论
    for comment in comments_list:
        print(comment["content"]["message"])


