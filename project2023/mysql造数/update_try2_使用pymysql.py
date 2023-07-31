import pymysql

# 连接到MySQL数据库
cnx = pymysql.connect(host='localhost', user='your_username', password='your_password', database='your_database')

# 创建一个光标对象
cursor = cnx.cursor()

# 更新数据的SQL查询
update_query = "UPDATE your_table SET column1 = %s, column2 = %s WHERE id = %s"

# 提供要更新的数据
new_column1_value = 'New Value 1'
new_column2_value = 'New Value 2'
row_id = 1

# 执行更新查询
cursor.execute(update_query, (new_column1_value, new_column2_value, row_id))

# 提交更改到数据库
cnx.commit()

# 关闭光标和数据库连接
cursor.close()
cnx.close()
