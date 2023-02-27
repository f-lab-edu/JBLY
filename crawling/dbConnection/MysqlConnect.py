import pymysql


def connect(products):
    # productsData order = storeName, itemName, imageUrl, price, itemType, shopId
    connect = pymysql.connect(host='localhost', user='root', password='thwjd123', db='jbly', charset='utf8')
    cursor = connect.cursor()

    sql = "INSERT INTO product (shopName, productName, image, price, productType, shopId) VALUES (%s, %s, %s, %s, %s, %s)"

    for product in products:
        storeName, itemName, imageUrl, price, type, shopId = product
        try:
            cursor.execute(sql, (storeName, itemName, imageUrl, price, type, shopId))
        except:
            print(storeName, itemName, imageUrl, price, type, shopId)
    connect.commit()
    cursor.close()
    connect.close()
    return None
