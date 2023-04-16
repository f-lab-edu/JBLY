from dbConnection import mysql_connect
import logging

logging.basicConfig(level=logging.INFO)

def insert_product_not_exist(products):
    connectedDb = mysql_connect.connect()

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

 # multi row insert, mysql쿼리는 반복문x, connectionpool만들거나 multirow, (상품 하나 돌고 확인하고 인서트 하나돌고 확인하고 인서트)
    # 성능 모니터링

    connectedDb.commit()
    cursor.close()
    mysql_connect.disconnect(connectedDb)

    return None

# cloud db에 존재하는 데이터 전부를 가져옵니다. product_query 안에서 사용되는 메서드입니다.
def get_whole_data_from_db():
    connect = mysql_connect.connect()

    query = "select * from product"
    cursor = connect.cursor()

    cursor.execute(query)
    total_product_data = cursor.fetchall()

    return list(map(lambda sub_list : sub_list[1:], total_product_data))