import requests

url = "http://example.com/api/endpoint"
data = {"key1": "value1", "key2": "value2"}
token = "your_token_here"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("请求成功")
    print(response.text)
else:
    print("请求失败")
    print("状态码:", response.status_code)
