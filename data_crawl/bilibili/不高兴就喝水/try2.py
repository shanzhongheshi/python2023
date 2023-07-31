from time import sleep
import requests
from selenium import webdriver
from lxml import etree

urls=[]
oids=[]
data_list=[]
def get_url():
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    # js=requests.get("https://api.bilibili.com/x/space/arc/search?mid=2026561407&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp",headers=head).json()
    js=requests.get("https://api.bilibili.com/x/space/wbi/arc/search?mid=2026561407&pn=1&ps=25&index=1&order=pubdate&order_avoided=true&platform=web&web_location=1550101&w_rid=0317c73452f81a1e1731e34e6dddbe7b&wts=1680524645",headers=head).json()
    for i in js["data"]["list"]["vlist"]:
        urls.append("https://www.bilibili.com/video/"+i["bvid"])
        oids.append(i["aid"])
    return urls,oids

def parser_data(url):
    dic = {}
    bro = webdriver.Chrome()
    bro.get(url)
    bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 向下拉动一屏
    sleep(4)
    bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 向下拉动一屏
    sleep(4)
    bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 向下拉动一屏
    sleep(4)
    #page_source  获取源码
    html=etree.HTML(bro.page_source)
    print(html)
    try:
        dic["title"]=html.xpath('//div[@id="viewbox_report"]/h1/@title')[0]
    except:
        dic["title"]=""
    try:
        dic["view"]=html.xpath('//span[@class="view"]/text()')[0]
    except:
        dic["view"]=""
    try:
        dic["dm"]=html.xpath('//span[@class="dm"]/text()')[0]
    except:
        dic["dm"]=""
    try:
        dic["page"]=html.xpath('//*[@id="comment"]/div/div[2]/div/div[4]/a[last()-1]/text()')[0]
    except:
        dic["page"]="1"
    data_list.append(dic)
    bro.quit()

if __name__ == '__main__':

    urls,oids=get_url()
    for url in urls:
        data_list=parser_data(url)
        print(data_list)
        break
