def insertProductIsNotExist(connectedDb, products):
    insertSql = "INSERT INTO product (shopName, productName, image, price, productType, detailInfo, shopId, " \
                "detailHtml) SELECT %s, %s, %s, %s, %s, %s, %s, %s FROM DUAL WHERE NOT EXISTS (SELECT * FROM product " \
                "WHERE shopId=%s AND productName=%s) "

    cursor = connectedDb.cursor()

    for product in products:
        storeName, itemName, imageUrl, price, type, detailInfo, shopId, detailHtml = product
        try:
            cursor.execute(insertSql, (
            storeName, itemName, imageUrl, price, type, detailInfo, shopId, detailHtml, shopId, itemName))
        except:
            continue

    connectedDb.commit()
    cursor.close()
    return None
