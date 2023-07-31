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

# 转换为字符串并打印结果
for row in results:
    # 将每个字段转换为字符串，并用分号分隔
    row_str = ";".join(str(field) for field in row)
    print(row_str)

# 关闭游标和数据库连接
cursor.close()
conn.close()
