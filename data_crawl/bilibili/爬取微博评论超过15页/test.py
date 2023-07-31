import requests as re
import  json


url='https://m.weibo.cn/comments/hotflow?id=4910425785768847&mid=4910425785768847&max_id=585407462046845&max_id_type=0'
# url="https://m.weibo.cn/comments/hotflow?id=4907928123605557&mid=4907928123605557&max_id_type=0"
headers={
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",
    "Cookie": "SCF=AlyYCUTSNP67WvyClzxK7WVOYg-I3xwX71ESRR4UjTPC743AlS_VJFP__2x7nQGDkTGeTIYw-IqdE-95CFvQx58.; WEIBOCN_FROM=1110006030; loginScene=102003; SUB=_2A25JgeGbDeRhGeRO41AT8C7Jzj2IHXVqjY_TrDV6PUJbkdAGLUT_kW1NUEmRQA_ZBs3HLsomDNlBdE7uRpc6QcvH; _T_WM=79687871621; XSRF-TOKEN=b314fb; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4910425785768847%26luicode%3D20000061%26lfid%3D4910425785768847%26uicode%3D20000061%26fid%3D4910425785768847"
}
response=re.get(url,headers)
print(response)
print(response.text)