import pymysql
import os

def connector():
    cloud_host = os.environ.get("DB_HOST")
    cloud_user = os.environ.get("DB_USER")
    cloud_pwd = os.environ.get("DB_PWD")
    cloud_name = os.environ.get("DB_NAME")
    cloud_port = os.environ.get("DB_PORT")

    cloud_port = int(cloud_port)

    # column 이름이 key값으로 들어간 형태로 {key : value} 반환합니다.
    return pymysql.connect(host=cloud_host,
                           user=cloud_user,
                           password=cloud_pwd,
                           db=cloud_name,
                           charset='utf8',
                           port=cloud_port,
                           cursorclass=pymysql.cursors.DictCursor
                           )