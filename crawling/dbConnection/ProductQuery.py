from dbConnection import MysqlConnect
import logging

logging.basicConfig(level=logging.INFO)

def insertProductIsNotExist(products):
    connectedDb = MysqlConnect.connect()

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
            logging.info(storeName + "의 상품 " + itemName + "이 DB에 적재되지 않았습니다.")

    connectedDb.commit()
    cursor.close()
    MysqlConnect.disconnect(connectedDb)

    return None
