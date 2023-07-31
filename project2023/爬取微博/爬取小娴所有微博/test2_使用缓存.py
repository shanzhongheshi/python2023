import requests_cache
import mysql.connector
import requests

#pip install requests_cache mysql-connector-python
# 配置MySQL数据库连接信息
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'python',
}

# 创建MySQL数据库连接
cnx = mysql.connector.connect(**db_config)

# 创建MySQL表
cursor = cnx.cursor()
create_table_query = """
    CREATE TABLE IF NOT EXISTS cache (
        url VARCHAR(255) PRIMARY KEY,
        response BLOB
    )
"""
cursor.execute(create_table_query)

# 配置requests_cache使用MySQL缓存
requests_cache.install_cache('mysql_cache', backend='mysql', connection=cnx)

# 进行请求
response = requests.get('https://www.baidu.com')

# 关闭数据库连接
cnx.close()
