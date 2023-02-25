import pymysql


def connect(products):
    # productsData order = storeName, itemName, imageUrl, price, itemType
    connect = pymysql.connect(host='localhost', user='root', password='1234', db='test', charset='utf8')
    cursor = connect.cursor()

    sql = "INSERT INTO product (storeName, productName, image, price, itemType, shopId) VALUES (%s, %s, %s, %s, %s, %s)"

    for product in products:
        storeName, itemName, imageUrl, price, itemType, shopId = product
        cursor.execute(sql, (storeName, itemName, imageUrl, price, itemType, shopId))

    connect.commit()
    cursor.close()
    connect.close()
    return None
