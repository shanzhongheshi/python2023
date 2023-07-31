import requests
import  re
#导入json模块
import  json
#导入格式化模块
from pprint import pprint
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer":"https://www.bilibili.com/",
    "Cookie":"CURRENT_BLACKGAP=0; blackside_state=0; LIVE_BUVID=AUTO6016500812878695; i-wanna-go-back=-1; buvid_fp_plain=undefined; fingerprint3=bf9893de521869230395b5160ff8e960; is-2022-channel=1; buvid4=4167975E-CC0F-8C84-55BE-49A6B12078B866585-022012418-g%2FJDFC92Uz9yEk%2BwWggH8A%3D%3D; hit-new-style-dyn=0; rpdid=|(u)~lJ|lkkk0J'uYY))lR~Y); fingerprint=80f4ab1021d0be2236355d8faa92dfff; DedeUserID=356358242; DedeUserID__ckMd5=e3f9e79e979e1824; b_ut=5; buvid3=62BA43EB-A339-CC19-1BF7-010FEFF4194465112infoc; b_nut=1670499465; _uuid=7FA32DC9-47E3-F410A-3FA6-AA10102BB44EF765308infoc; buvid_fp=80f4ab1021d0be2236355d8faa92dfff; CURRENT_FNVAL=16; nostalgia_conf=-1; CURRENT_PID=250bb440-c8a0-11ed-b690-1b868cd28c0c; hit-dyn-v2=1; home_feed_column=5; browser_resolution=1536-731; CURRENT_QUALITY=64; bsource=search_baidu; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; SESSDATA=2040b03a%2C1703073272%2C6422d%2A61XqjVqqpqPuBSoCh7ZyzMBiXd3dewUyHFCmM5bsg4_A9PZTY-0Alte6RFHdSYXs8tpEULlgAAKgA; bili_jct=cbf6b41c295d8e66e5e2ffb48ecbb070; sid=8s0hvo7i; b_lsid=10FCA636C_188E86D7682; bp_video_offset_356358242=810409751227662300; PVID=3"
}
url="https://www.bilibili.com/video/BV1bX4y1i7mk/"
response=requests.get(url=url,headers=headers)
# print(response.status_code)
# print(response.text)
title=re.findall('"title":"(.*?)"',response.text)[0]
video_info=re.findall('<script>window.__playinfo__=(.*?)</script>',response.text)[0]
#类型转换，将字符串转成字典
json_data=json.loads(video_info)
pprint(json_data)
audio_url=json_data["data"]["dash"]["audio"][0]["baseUrl"]#音频文件
print(audio_url)
video_url=json_data["data"]["dash"]["video"][0]["baseUrl"]
print(video_url)

#TODO  保存数据
audio_content=requests.get(url=audio_url,headers=headers).content
video_content=requests.get(url=video_info,headers=headers).content
with open('video\\'+ title+'.mp3',mode='wb') as a:
    a.write(audio_content)
with open('video\\'+ title+'.mp4',mode='wb') as v:
    v.write(video_content)