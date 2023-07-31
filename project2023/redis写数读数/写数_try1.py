# # pip install redis-py
# import redis
#
# # 创建 Redis 连接
# redis_host = 'localhost'  # Redis 服务器地址
# redis_port = 6379  # Redis 端口号
# redis_db = 0  # Redis 数据库编号
# redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
#
# # 写入数据
# for i in range(10000):
#     key = f'my_table:{i}'  # 每条数据的键名
#     value = f'value_{i}'  # 每条数据的值
#     redis_client.set(key, value)
#
# # 关闭 Redis 连接
# redis_client.close()
