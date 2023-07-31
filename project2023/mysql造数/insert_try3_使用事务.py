import pymysql

# 连接到MySQL数据库
cnx = pymysql.connect(host='localhost', user='your_username', password='your_password', database='your_database')

# 创建一个光标对象
cursor = cnx.cursor()

try:
    # 开始事务
    cnx.begin()

    # 循环插入数据
    for i in range(1, 10001):
        student_id = i
        name = f"学生 {i}"
        age = 18 + (i % 5)  # 年龄范围在18到22岁之间
        gender = "男" if i % 2 == 0 else "女"
        score = 60 + (i % 41)  # 成绩范围在60到100之间
        address = f"地址 {i}"
        interests = f"兴趣 {i}"
        insert_query = '''
        INSERT INTO students (student_id, name, age, gender, score, address, interests)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (student_id, name, age, gender, score, address, interests))

    # 提交事务
    cnx.commit()
    print("数据插入成功")

except Exception as e:
    # 发生错误时回滚事务
    cnx.rollback()
    print("插入数据时出现错误:", str(e))

finally:
    # 关闭光标和数据库连接
    cursor.close()
    cnx.close()
