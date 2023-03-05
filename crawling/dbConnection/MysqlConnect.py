from dbConnection import MysqlConnectionInfo

def connect(products):

    # productsData order = storeName, itemName, imageUrl, price, itemType, detailInfo, shopId
    connector = MysqlConnectionInfo.connector()
    cursor = connector.cursor()

    sql = "INSERT INTO product (shopName, productName, image, price, productType, detailInfo shopId) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    for product in products:
        storeName, itemName, imageUrl, price, type, detailInfo, shopId = product
        try:
            cursor.execute(sql, (storeName, itemName, imageUrl, price, type, detailInfo, shopId))
        except:
            print(storeName, itemName, imageUrl, price, type, detailInfo, shopId)
    connector.commit()
    cursor.close()
    connector.close()
    return None
