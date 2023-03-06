from dbConnection import MysqlConnectionInfo

# todo 책임 분리
def connect(products):
    # productsData order = storeName, itemName, imageUrl, price, itemType, detailInfo, shopId
    connector = MysqlConnectionInfo.connector()
    cursor = connector.cursor()

    insertSql = "INSERT INTO product (shopName, productName, image, price, productType, detailInfo shopId) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    selectSql = "SELECT * FROM product WHERE shopId=%s AND productName=%s"


    for product in products:
        storeName, itemName, imageUrl, price, type, detailInfo, shopId = product

        cursor.execute(selectSql, (shopId, itemName))
        result = cursor.fetchone()

        if not result:
            try:
                cursor.execute(insertSql, (storeName, itemName, imageUrl, price, type, detailInfo, shopId))
            except:
                print(storeName, itemName, imageUrl, price, type, detailInfo, shopId)
    connector.commit()
    cursor.close()
    connector.close()
    return None