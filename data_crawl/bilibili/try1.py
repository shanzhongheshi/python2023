import requests  # 发送请求
import pandas as pd  # 保存csv文件
import os  # 判断文件是否存在
import time
from time import sleep  # 设置等待，防止反爬
import random  # 生成随机数


# 请求头
headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 需定期更换cookie，否则location爬不到
    'cookie': "CURRENT_BLACKGAP=0; blackside_state=0; nostalgia_conf=-1; hit-dyn-v2=1; LIVE_BUVID=AUTO6016500812878695; go_old_video=1; i-wanna-go-back=-1; buvid_fp_plain=undefined; fingerprint3=bf9893de521869230395b5160ff8e960; is-2022-channel=1; buvid4=4167975E-CC0F-8C84-55BE-49A6B12078B866585-022012418-g%2FJDFC92Uz9yEk%2BwWggH8A%3D%3D; hit-new-style-dyn=0; rpdid=|(u)~lJ|lkkk0J'uYY))lR~Y); fingerprint=80f4ab1021d0be2236355d8faa92dfff; DedeUserID=356358242; DedeUserID__ckMd5=e3f9e79e979e1824; CURRENT_QUALITY=80; b_ut=5; buvid3=62BA43EB-A339-CC19-1BF7-010FEFF4194465112infoc; b_nut=1670499465; _uuid=7FA32DC9-47E3-F410A-3FA6-AA10102BB44EF765308infoc; buvid_fp=80f4ab1021d0be2236355d8faa92dfff; CURRENT_FNVAL=16; header_theme_version=CLOSE; home_feed_column=5; SESSDATA=c43edbbc%2C1692881216%2C948ed%2A21; bili_jct=3feda0b61082857738bca911a0895bf9; sid=73obamp9; bp_video_offset_356358242=766619549071048700; b_lsid=B10F8688C_1868B52ACB1; bsource=search_baidu; PVID=2",
    'origin': 'https://www.bilibili.com&;#39;',
    'referer': 'https://www.bilibili.com/video/BV1FG4y1Z7po/?spm_id_from=333.337.search-card.all.click&;amp;vd_source=69a50ad969074af9e79ad13b34b1a548',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}


