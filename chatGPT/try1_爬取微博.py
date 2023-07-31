import requests
from bs4 import BeautifulSoup

# 指定微博博主的主页链接
url = 'https://www.weibo.com/hanlu235959'

# 添加User-Agent头信息，伪装成浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 获取主页的HTML源码
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# 获取微博博主的用户ID，用于构造访问API的链接
#user_id = soup.find(attrs={'node-type': 'feed_list_top'}).attrs['tbinfo'][6:]
# print(user_id)
user_id='1192966660'
# 构造访问API的链接
api_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid=107603{}'.format(user_id, user_id)

# 定义一个空列表，用于存储所有微博内容
weibo_list = []

# 循环访问API的所有页面，直到无法获取新的微博
while True:
    # 获取API的JSON数据
    response = requests.get(api_url, headers=headers)
    data = response.json()

    # 获取当前页面的所有微博内容
    cards = data['data']['cards']
    print(cards)
    for card in cards:
        # 过滤出原创微博
        if 'mblog' in card:
            weibo = card['mblog']['text']
            weibo_list.append(weibo)

    # 检查是否还有下一页
    # if data['data']['cardlistInfo']['page'] >= data['data']['cardlistInfo']['totalpage']:
    #     break

    # 构造下一页的API链接
    # api_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid=107603{}&page={}'.format(
    #     user_id, user_id, data['data']['cardlistInfo']['page'] + 1)

# 打印所有微博内容
for weibo in weibo_list:
    print(weibo)
    print(1)