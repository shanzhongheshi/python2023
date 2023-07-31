import requests
from bs4 import BeautifulSoup
#https://www.weibo.com/ajax/statuses/buildComments?is_reload=1&id=4912454217237229&is_show_bulletin=2&is_mix=0&count=10&uid=1192966660&fetch_level=0
def fetchUrl():
    # url
    url = "https://weibo.com/ajax/statuses/buildComments"
    # 请求头
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    }
    # 参数
    params = {
        "is_reload" : 1,
        "id" : 4912454217237229,
        "is_show_bulletin" : 2,
        "is_mix" : 0,
        "count" : 10,
        "uid" : 1192966660,
        "fetch_level":0
    }

    r = requests.get(url, headers = headers, params = params)
    return r.json()

if __name__ == '__main__':
    jsonObj=fetchUrl()
    data = jsonObj["data"]
    for item in data:
        # 评论id
        comment_Id = item["id"]
        # 评论内容
        content = BeautifulSoup(item["text"], "html.parser").text
        print(content)
        # 评论时间
        created_at = item["created_at"]
        # 点赞数
        like_counts = item["like_counts"]
        # 评论数
        total_number = item["total_number"]
        # 评论者 id
        userID = item["user"]["id"]
        # 评论者昵称
        # userName = item["user"]["name"]
        # 评论者城市
        userCity = item["user"]["location"]

