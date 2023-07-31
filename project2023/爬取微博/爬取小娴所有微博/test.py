import  datetime
def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT='%a %b %d %H:%M:%S +0800 %Y'
    timeArray=datetime.datetime.strptime(v_str,GMT_FORMAT)
    ret_time=timeArray.strftime("%Y-%m-%d  %H:%M:%S")
    print(ret_time)


v_str="Thu Jun 20 11:15:51 +0800 2019"
trans_time(v_str)
