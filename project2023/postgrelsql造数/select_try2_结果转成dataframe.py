import pandas as pd
import psycopg2

# 连接到 PostgreSQL 数据库
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_user",
    password="your_password"
)

# 创建一个游标对象
cursor = conn.cursor()

# 执行查询语句
query = "SELECT * FROM your_table LIMIT 5;"
cursor.execute(query)

# 获取查询结果的前5条数据
results = cursor.fetchmany(5)

# 将结果转换为DataFrame
df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])

# 设置显示选项
pd.set_option("display.max_columns", None)

# 打印DataFrame
print(df)

# 关闭游标和数据库连接
cursor.close()
conn.close()
