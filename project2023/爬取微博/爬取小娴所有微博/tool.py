import requests_cache
import datetime


def cache():
    requests_cache.install_cache()
    requests_cache.clear()

#时间格式转换
def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT='%a %b %d %H:%M:%S +0800 %Y'
    timeArray=datetime.datetime.strptime(v_str,GMT_FORMAT)
    ret_time=timeArray.strftime("%Y-%m-%d  %H:%M:%S")
    return  ret_time