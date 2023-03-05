from crawling.dbConnection import MysqlConnectionInfo


def connect(products):
    # productsData order = storeName, itemName, imageUrl, price, itemType, shopId
    connector = MysqlConnectionInfo.connector()
    cursor = connector.cursor()

    sql = "INSERT INTO product (shopName, productName, image, price, productType, shopId) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    for product in products:
        storeName, itemName, imageUrl, price, type, shopId, detailInfo = product
        try:
            cursor.execute(sql, (storeName, itemName, imageUrl, price, type, shopId, detailInfo))
        except:
            print(storeName, itemName, imageUrl, price, type, shopId, detailInfo)
    connector.commit()
    cursor.close()
    connector.close()
    return None
