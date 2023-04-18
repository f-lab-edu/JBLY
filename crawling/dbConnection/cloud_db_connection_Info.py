import pymysql
import os

def connector():
    cloudHost = os.environ.get("DB_HOST")
    cloudUser = os.environ.get("DB_USER")
    cloudPwd = os.environ.get("DB_PWD")
    cloudName = os.environ.get("DB_NAME")
    cloudPort = os.environ.get("DB_PORT")

    cloudPort = int(cloudPort)

    # column 이름이 key값으로 들어간 형태로 {key : value} 반환합니다.
    return pymysql.connect(host=cloudHost,
                           user=cloudUser,
                           password=cloudPwd,
                           db=cloudName,
                           charset='utf8',
                           port=cloudPort,
                           cursorclass=pymysql.cursors.DictCursor
                           )