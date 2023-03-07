
def insertProducts(connectedDb, products):
    insertSql = "INSERT INTO product (shopName, productName, image, price, productType, detailInfo shopId) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor = connectedDb.cursor()

    for product in products:
        storeName, itemName, imageUrl, price, type, detailInfo, shopId = product
        try:
            cursor.execute(insertSql, (storeName, itemName, imageUrl, price, type, detailInfo, shopId))
        except:
            continue
    connectedDb.commit()
    cursor.close()
    return None

def checkDuplicatedProducts(connectedDb, products):
    result = []
    selectSql = "SELECT * FROM product WHERE shopId=%s AND productName=%s"

    cursor = connectedDb.cursor()

    for product in products:
        storeName, itemName, imageUrl, price, type, detailInfo, shopId = product
        cursor.execute(selectSql, (shopId, itemName))
        getProduct = cursor.fetchone()

        if not getProduct:
            result.append(product)

    connectedDb.commit()
    cursor.close()

    return result