import pymysql

def mysqlconnect():

    return pymysql.connect(host='localhost', user='root', password='thwjd123', db='jbly', charset='utf8')