import pymysql


def connect():
    connect = pymysql.connect(host='localhost', user='root', password='1234', db='jbly', charset='utf8')
    cursor = connect.cursor()

    cursor.execute("select * from user")
    data = cursor.fetchall()
    print(data)
    connect.close()
