import pymysql


def testConnect():
    connect = pymysql.connect(host='localhost', user='root', password='1234', db='test', charset='utf8')
    cursor = connect.cursor()

    sql = "INSERT INTO professor (name, belong, phone) VALUES (%s, %s, %s)"

    cursor.execute(sql, ('유재석', 'IDE', '01112345678'))
    cursor.execute(sql, ('황영조', 'MSE', '01121342443'))
    cursor.execute(sql, ('케이멀', 'ESE', '01123424343'))
    cursor.execute(sql, ('리오넬', 'IDE', '01123432432'))

    connect.commit()

    selectSql = "select * from professor;"

    cursor.execute(selectSql)
    data = cursor.fetchall()
    print(data)

    cursor.close()
    connect.close()
