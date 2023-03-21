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

 # multi row insert, mysql쿼리는 반복문x, connectionpool만들거나 multirow, (상품 하나 돌고 확인하고 인서트 하나돌고 확인하고 인서트)
    # 성능 모니터링

    connectedDb.commit()
    cursor.close()
    return None
