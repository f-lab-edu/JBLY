import pymysql
import os

def connector():
    cloudHost = os.environ.get("DB_HOST")
    cloudUser = os.environ.get("DB_USER")
    cloudPwd = os.environ.get("DB_PWD")
    cloudName = os.environ.get("DB_NAME")
    cloudPort = os.environ.get("DB_PORT")

    cloudPort = int(cloudPort)

    return pymysql.connect(host=cloudHost,
                           user=cloudUser,
                           password=cloudPwd,
                           db=cloudName,
                           charset='utf8',
                           port=cloudPort)
