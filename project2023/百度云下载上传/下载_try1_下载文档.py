import requests

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print('下载完成！')
    else:
        print('下载失败。')

# 要下载的文档的链接
file_url = 'https://pan.baidu.com/s/your_file_id'

# 下载文档并保存到本地的路径
save_path = '/path/to/save/file.docx'

# 调用下载函数
download_file(file_url, save_path)
