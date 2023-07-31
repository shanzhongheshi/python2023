import pymysql
import  time  #计算时间

start=time.time()
print("start_time:", start)
# 连接到MySQL数据库
cnx = pymysql.connect(host='localhost', user='root', password='root', database='python')

# 创建一个光标对象
cursor = cnx.cursor()

# 创建学生信息表
create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    score FLOAT,
    address VARCHAR(255),
    interests TEXT
)
'''

cursor.execute(create_table_query)

# 生成要插入的学生数据
students_data = []
for i in range(1, 10001):
    student_id = i
    name = f"学生 {i}"
    age = 18 + (i % 5)  # 年龄范围在18到22岁之间
    gender = "男" if i % 2 == 0 else "女"
    score = 60 + (i % 41)  # 成绩范围在60到100之间
    address = f"地址 {i}"
    interests = f"兴趣 {i}"
    student_data = (student_id, name, age, gender, score, address, interests)
    students_data.append(student_data)

# 插入学生数据
insert_query = '''
INSERT INTO students (student_id, name, age, gender, score, address, interests)
VALUES (%s, %s, %s, %s, %s, %s, %s)
'''

cursor.executemany(insert_query, students_data)

# 提交更改到数据库
cnx.commit()

# 关闭光标和数据库连接
cursor.close()
cnx.close()
end = time.time()    # 程序结束时间
print("end_time:", end)
run_time = end - start   # 程序的运行时间，单位为秒
print("run_time:", run_time)