import  requests as re

headers={
    "Host":"image.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer":"https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%BB%C6%C9%BD&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCw2LDQsMywxLDUsMiw4LDcsOQ%3D%3D",
    "Cookie":"BDqhfp=%E9%BB%84%E5%B1%B1%26%26NaN-1undefined%26%260%26%261; BIDUPSID=5F394AB31B93D27F3CB76510B9108253; PSTM=1638777811; __yjs_duid=1_fdf18ac8bf04ad7965b2b8ca0d6a58531639017345656; indexPageSugList=%5B%22%E6%A2%85%E9%95%BF%E8%8B%8F%20%20%E6%A8%A1%E4%BB%BF%22%2C%22%E6%A2%85%E9%95%BF%E8%8B%8F%20%20%E6%96%87%E6%9D%BE%22%2C%22%E6%A2%85%E9%95%BF%E8%8B%8F%20%20%E5%96%9C%E5%89%A7%E4%BA%BA%22%2C%22%E6%A2%85%E9%95%BF%E8%8B%8F%20cosplay%22%2C%22%E7%99%BE%E5%8F%98%E5%B0%8F%E6%A8%B1%20%E5%8F%98%E8%BA%AB%E5%8A%A8%E6%80%81%E5%9B%BE%22%2C%22%E8%AE%A1%E5%88%92%20%20logo%22%2C%22%E8%A7%84%E5%88%92%20%20logo%22%2C%22CASE%20logo%22%2C%22use%20CASE%20logo%22%5D; BAIDUID=5F394AB31B93D27F020F4F4877D759FC:SL=0:NR=10:FG=1; BDUSS=1Qa3FON2xBUXVLYllvOXVpUVJqdjZ0M3B4RjBtY21GRDZxZjI3QjhyME9DWU5pRVFBQUFBJCQAAAAAAAAAAAEAAABGaeohwda9-NDbMzIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA58W2IOfFtiVC; BDUSS_BFESS=1Qa3FON2xBUXVLYllvOXVpUVJqdjZ0M3B4RjBtY21GRDZxZjI3QjhyME9DWU5pRVFBQUFBJCQAAAAAAAAAAAEAAABGaeohwda9-NDbMzIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA58W2IOfFtiVC; MCITY=-131%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=5F394AB31B93D27F020F4F4877D759FC:SL=0:NR=10:FG=1; BA_HECTOR=ak00202l8la50525250025071i9ania1p; ZFY=lUwPb4:BOK4PXasYKnaxJtFNfheG0KqMiwWaKXozObw4:C; H_PS_PSSID=38516_36551_38687_38794_38908_38793_38812_38836_38636_26350_38570_22160; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_YjcwZjAwMDY4ZGIzZDUwZmM4NjExZWMzMjNlYzRjYWUzYzNkMWQ2MGYwYjM1ZDUxMThiNDEyMGRhY2ZlZTNjYTAxOWY0M2ZlYzc5NGY2NjQ1MjQ5Mzk3OTdmZmZjNjU2NTdmOTM4MDMwZThiOGFmNjA2ZTFkMmU3MDYzMzUxODVlNGZkNmE5ZDAwZjY0YWY3ZDA1YzM0ODY0N2E4ZjRkOGY3YzY5ZGVjNmZjN2E2NWYyZTRiNjI1YTYwNDlkMDMxYjUxY2JhNzA1NDUxMjFlYjAxZDE3NTc0MjdjODllMWE="
}
number=1
for page in range(1,11):
    # url=f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9752062745631324382&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E9%BB%84%E5%B1%B1&queryWord=%E9%BB%84%E5%B1%B1&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn={page*30}&rn=30&gsm=3c&1687522709064="
    url=f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10818268392694614038&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%80%AA%E5%A6%AE&cg=star&queryWord=%E5%80%AA%E5%A6%AE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={page}&rn=30&gsm=1e&1687524128632="
    response=re.get(url=url,headers=headers)
    json_data=response.json()
    data_list=json_data["data"]
    for data in data_list[:-1]:
        fromPageTitle=data["fromPageTitle"]
        middleURL=data["middleURL"]
        img_data=re.get(middleURL).content  #返回：response
        with open(f"img/{number}.jpg",mode="wb") as f:
            f.write(img_data)
        number+=1