import  requests

# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}
v_keyword="淄博烧烤"
page=3
# 请求地址
url = 'https://m.weibo.cn/api/container/getIndex'
# 请求参数
params = {
    "containerid": "100103type=60&q={}".format(v_keyword),
    "page_type": "searchall",
    "page": page
}
# 发送请求
r = requests.get(url, headers=headers, params=params)
cards = r.json()["data"]["cards"]
print('微博数量：', len(cards))
id_list_list=[]
for card in cards:
    # 微博id
    id_list = card['mblog']['id']
    id_list_list.append(id_list)

print(id_list_list)