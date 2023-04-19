from dbConnection import mysql_connect, MysqlConnectionInfo
import datetime
import logging

logging.basicConfig(level=logging.INFO)

# bulk insert를 통해 데이터를 cloud에 밀어넣습니다.
def insert_crawling_data(products):
    # conn = mysql_connect.connect()
    before_insert_data = datetime.datetime.now()
    before_insert_data_time = before_insert_data.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Data insert 전 시간 : {before_insert_data_time}")
    conn = MysqlConnectionInfo.cloud_db_connection()

    query = "INSERT INTO product (detailHtml, detailInfo, price, image, productName, productType, shopId, shopName)" \
            " values (%(detailHtml)s, %(detailInfo)s, %(price)s, %(image)s, %(productName)s, %(productType)s, %(shopId)s, %(shopName)s)"

    cursor = conn.cursor()
    cursor.executemany(query, products)
    conn.commit()
    conn.close()
    # mysql_connect.disconnect(conn)
    after_insert_data = datetime.datetime.now()
    after_insert_data_time = after_insert_data.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Data insert 후 시간 : {after_insert_data_time}")

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

def local_db_delete_id_column():
    key_to_remove = 'id'

    conn = MysqlConnectionInfo.local_db_connection()
    cursor = conn.cursor()
    query = "select * from product"
    cursor.execute(query)

    products = cursor.fetchall()
    products = list(map(lambda d: {k: v for k, v in d.items() if k != key_to_remove}, products)) # pk인 id를 제거합니다.
    return products
