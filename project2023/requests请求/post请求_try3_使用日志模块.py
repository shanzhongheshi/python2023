import requests
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO)

url = "http://example.com/api/endpoint"
data = {"key1": "value1", "key2": "value2"}

# 发送请求并记录日志
response = requests.post(url, data=data)
logging.info("请求发送成功")

if response.status_code == 200:
    logging.info("请求成功")
    logging.info(f"响应内容: {response.text}")
else:
    logging.error("请求失败")
    logging.error(f"状态码: {response.status_code}")
