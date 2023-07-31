import requests
import json

# 定义要爬取的微博的url
weibo_url = 'https://m.weibo.cn/api/comments/show?id=4885831775166181&page={}'  # 将 xxxxxxxxxx 替换为微博id

# 定义请求头，加上 User-Agent 可以伪装成浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}

# 定义一个空列表，用来存放所有评论
all_comments = []

# 爬取前 5 页评论
for page in range(1, 6):
    # 构造当前页的url
    url = weibo_url.format(page)
    print(url)

    # 发送请求
    response = requests.get(url, headers=headers)

    # 将响应转为json格式
    data = json.loads(response.text)

    # 获取评论列表
    comments = data['data']['data']

    # 遍历评论列表，将每个评论的text字段加入到all_comments列表中
    for comment in comments:
        all_comments.append(comment['text'])

# 打印所有评论
print(all_comments)