from dbConnection import MysqlConnectionInfo

def connect(products):
    # productsData order = storeName, itemName, imageUrl, price, itemType, detailInfo, shopId, detailHtml
    connector = MysqlConnectionInfo.connector()
    cursor = connector.cursor()

    sql = "INSERT INTO product (shopName, productName, image, price, productType, detailInfo, shopId, detailHtml) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    for product in products:
        storeName, itemName, imageUrl, price, type, detailInfo, shopId, detailHtml = product
        try:
            cursor.execute(sql, (storeName, itemName, imageUrl, price, type, detailInfo, shopId, detailHtml))
        except:
            print(storeName, itemName, imageUrl, price, type, detailInfo, shopId, detailHtml)
    connector.commit()
    cursor.close()
    connector.close()
    return None
