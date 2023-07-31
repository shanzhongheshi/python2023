import pymysql
from faker import Faker
import time
start = time.time()    # 程序开始时间,单位为秒
print("start_time:", start)

conn = pymysql.connect(
                       host="localhost",
                       port=3306,
                       user="root",
                       password="root",
                       db="python",
                       charset="utf8"
                       )  #获取连接

cursor = conn.cursor()    #获取游标
sql1 = """drop table if exists faker_user"""
sql2 = """
create table faker_user(
pid int primary key auto_increment,
username varchar(20),
password varchar(20),
address varchar(35) ,
identy varchar(50),
company varchar(300)
)
"""
cursor.execute(sql1)
cursor.execute(sql2)
fake = Faker("zh-CN")  #参数 locale：为生成数据的文化选项（语种），默认为 en_US，只有使用了相关文化，才能生成相对应的随机信息
for i in range(10000):
    sql = """insert into faker_user(username,password,address,identy,company) 
    values('%s','%s','%s','%s','%s')""" % (fake.name(), fake.password(special_chars=False), fake.address(),fake.ssn(),fake.company())
    print('姓名:'+fake.name() + '|密码:'+fake.password(special_chars=False) + '|地址:'+fake.address())
    cursor.execute(sql)

conn.commit()  #提交
cursor.close()
conn.close()

end = time.time()    # 程序结束时间
print("end_time:", end)
run_time = end - start   # 程序的运行时间，单位为秒
print("run_time:", run_time)