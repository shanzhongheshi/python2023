import pandas as pd
import numpy as np
import re  #正则

file_path = 'C:/Users/86906/Desktop/1.xlsx'
sheet_name = 'Sheet1'  # Replace with your sheet name
df = pd.read_excel(file_path, sheet_name=sheet_name,header=0)
data = df.values  #只读取excel中的值，不读取序号
print(df)
resource = list(np.concatenate(data.reshape((-1, 1), order="F")))  #将读取的数据转换为list

print(resource)  #打印list
