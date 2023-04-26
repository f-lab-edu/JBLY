import pymysql
import os
from mysql.connector import pooling

def cloud_db_connection():
    cloud_host = os.environ.get("DB_HOST")
    cloud_user = os.environ.get("DB_USER")
    cloud_pwd = os.environ.get("DB_PWD")
    cloud_name = os.environ.get("DB_NAME")
    cloud_port = os.environ.get("DB_PORT")
    cloud_port = int(cloud_port)

    config = {
        'host' : cloud_host,
        'user' : cloud_user,
        'password' : cloud_pwd,
        'database' : cloud_name,
    }

    return pooling.MySQLConnectionPool(pool_name='mypool', pool_size=12, **config)