# import mysql.connector
# """
# pip install aliyun-python-sdk-core
# pip install aliyun-python-sdk-oss2
# """
# import oss2
#
# # 配置阿里云OSS凭证
# access_key_id = 'your_access_key_id'
# access_key_secret = 'your_access_key_secret'
# endpoint = 'your_oss_endpoint'
# bucket_name = 'your_bucket_name'
#
# auth = oss2.Auth(access_key_id, access_key_secret)
# bucket = oss2.Bucket(auth, endpoint, bucket_name)
#
# # 建立MySQL数据库连接
# conn = mysql.connector.connect(
#     host='localhost',
#     user='your_username',
#     password='your_password',
#     database='your_database'
# )
# cursor = conn.cursor()
#
# # 上传图片并记录到表中
# def upload_image_and_record(file_path, description):
#     # 上传图片到OSS
#     remote_filename = oss2.utils.to_unicode(os.path.basename(file_path))
#     bucket.put_object_from_file(remote_filename, file_path)
#
#     # 记录图片信息到表中
#     insert_sql = "INSERT INTO images (description, storage_path) VALUES (%s, %s)"
#     storage_path = f"https://{bucket_name}.{endpoint}/{remote_filename}"
#     cursor.execute(insert_sql, (description, storage_path))
#     conn.commit()
#
# # 示例调用
# file_path = 'path/to/image.jpg'
# description = 'This is an image'
# upload_image_and_record(file_path, description)
#
# # 关闭数据库连接
# cursor.close()
# conn.close()
