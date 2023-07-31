import requests

url = "http://example.com/api/endpoint"
data = {"key1": "value1", "key2": "value2"}

response = requests.post(url, data=data)

# 打印请求参数
print(response.request.headers)
print(response.request.body)
