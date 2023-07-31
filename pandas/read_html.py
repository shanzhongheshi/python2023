import pandas as pd   # 导入库
url = 'http://weather.sina.com.cn/china/shanghaishi/'  # 目标网址(含有<table>的表格)
# df = pd.read_html(url)[1]
df = pd.read_html(url)[1]
print(df)