import mysql.connector

# 建立MySQL数据库连接
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

# 创建游标对象
cursor = conn.cursor()

# 执行查询语句
sql = "SELECT image_data FROM images WHERE image_id = %s"
image_id = 1  # 假设要检索的图片的ID为1
cursor.execute(sql, (image_id,))

# 获取查询结果
result = cursor.fetchone()
image_data = result[0]

# 将图片数据保存为文件
with open('retrieved_image.jpg', 'wb') as file:
    file.write(image_data)

# 关闭数据库连接
cursor.close()
conn.close()
