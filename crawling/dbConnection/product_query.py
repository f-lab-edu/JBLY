from dbConnection import mysql_connect
import logging

logging.basicConfig(level=logging.INFO)

# bulk insert를 통해 데이터를 cloud에 밀어넣습니다.
def insert_crawling_data(products):
    conn = mysql_connect.connect()

    query = "INSERT INTO product (detailHtml, detailInfo, price, image, productName, productType, shopId, shopName)" \
            " values (%(detailHtml)s, %(detailInfo)s, %(price)s, %(image)s, %(productName)s, %(shopName)s, %(productType)s, %(shopId)s)"

    cursor = conn.cursor()
    cursor.executemany(query, products)
    conn.commit()
    mysql_connect.disconnect(conn)

    return None

# cloud db에 존재하는 데이터 전부를 가져옵니다. 새로운 데이터를 판별할 때 사용되는 메서드입니다.
def get_whole_image_url_data_from_db():
    connect = mysql_connect.connect()
    query = "select image from product"
    cursor = connect.cursor()
    cursor.execute(query)
    image_data = cursor.fetchall()
    connect.close()
    return image_data
