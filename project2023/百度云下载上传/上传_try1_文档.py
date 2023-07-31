# #要向百度云上传文档，你可以使用百度云提供的开放接口来实现。百度云提供了 BaiduPCS-Py 这个 Python SDK，用于与百度云存储服务进行交互。
# #pip install baidupcs-py
# from baidupcs_py.baidupcs import BaiduPCSApi
#
# def upload_file(file_path, remote_path):
#     pcs = BaiduPCSApi()
#     pcs.upload(file_path, remote_path)
#     print('上传完成！')
#
# # 要上传的本地文件路径
# local_file_path = '/path/to/local/file.docx'
#
# # 在百度云中的远程路径，可以是文件夹或者文件名
# remote_file_path = '/path/in/baidu/cloud/file.docx'
#
# # 调用上传函数
# upload_file(local_file_path, remote_file_path)
