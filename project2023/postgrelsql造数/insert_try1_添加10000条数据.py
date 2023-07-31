import psycopg2  #pip install psycopg2
import random
import string

# 连接到PostgreSQL数据库
conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_username",
    password="your_password"
)

# 创建游标对象
cur = conn.cursor()

# 创建学生基本信息表
create_table_query = '''
    CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INTEGER,
        gender VARCHAR(10),
        address VARCHAR(100)
    );
'''
cur.execute(create_table_query)

# 生成随机数据并插入表中
for _ in range(10000):
    name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    age = random.randint(18, 25)
    gender = random.choice(['Male', 'Female'])
    address = ''.join(random.choice(string.ascii_letters) for _ in range(20))

    insert_query = '''
        INSERT INTO students (name, age, gender, address)
        VALUES (%s, %s, %s, %s);
    '''
    cur.execute(insert_query, (name, age, gender, address))

# 提交事务并关闭连接
conn.commit()
cur.close()
conn.close()
