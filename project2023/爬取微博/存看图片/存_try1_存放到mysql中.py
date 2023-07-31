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

# 创建图片表
create_table_sql = '''
    CREATE TABLE IF NOT EXISTS images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        image_data LONGBLOB
    )
'''
cursor.execute(create_table_sql)

# 关闭数据库连接
cursor.close()
conn.close()
