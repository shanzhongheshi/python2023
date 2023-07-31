import requests
#https://weibo.com/ajax/friendships/friends?page=1&uid=1192966660
#https://weibo.com/ajax/friendships/friends?page=2&uid=1192966660

headers={
    "referer": "https://weibo.com/u/page/follow/1192966660",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",
    "cookie": "SINAGLOBAL=1863967907911.2815.1639802230789; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWO9cJpHbMEfRKRU2AaxlnC5JpX5KMhUgL.Foz71hzEeh5fSK22dJLoIp8KUgf_9PiW9rxLMJ4adc4kP7tt; ULV=1687575773554:24:6:3:5087122242554.023.1687575773474:1687482181673; XSRF-TOKEN=slpVuA13RzHGCPZSLumVdjr2; ALF=1690289731; SSOLoginState=1687697731; SCF=AlyYCUTSNP67WvyClzxK7WVOYg-I3xwX71ESRR4UjTPCO95nZzK11iqehCJCZr_FPtbDLTjqEYnOeI4YMESp1NY.; SUB=_2A25JnEkUDeRhGeRO41AT8C7Jzj2IHXVq6D3crDV8PUNbmtAGLWn2kW9NUEmRQBbxNzR9-3epaRG_8oLudEjX0grF; WBPSESS=Kk15ov95J8WHQrCkca4auO5svOnPep0T7UplebD51dSi5a6BzsjqgyipDma5gOXGzb4QBOVooEkk0UtF55N5_9MjBl2jQ7s_GvHfovfZfQhHOFheMu0omCQJ6Ucgbhxrx0YeQMHEPraFQ9pTozloRQ=="
}
url="https://weibo.com/ajax/friendships/friends?page=1&uid=1192966660"
response=requests.get(url=url,headers=headers)
# print(response.json())
data_json=response.json()
users_list=data_json["users"]
for user in users_list:
    print(user)
    print(user["name"],user["location"],user["followers_count"],user["verified_reason"])
    # break