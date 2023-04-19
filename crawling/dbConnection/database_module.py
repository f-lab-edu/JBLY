from dbConnection import MysqlConnectionInfo, product_query
import concurrent.futures
import logging

logging.basicConfig(level=logging.INFO)

'''
DB 관련 처리 작업은 이곳 database_module에서 담당합니다.
'''

pool = MysqlConnectionInfo.cloud_db_connection()

def run(crawling_datas):
    batch_size = 400
    db_image_datas = get_whole_image_url_data_from_cloud() # 이전에 크롤링된 데이터를 가져옵니다.
    products = check_duplicate_data(crawling_datas, db_image_datas) # 크롤링한 데이터와 이전 크롤링한 데이터를 비교해 새 상품일 경우 Insert를 진행합니다.

    '''
    500개로 쪼개진 데이터 셋을 map에 넘겨 Thread에 일을 할당합니다.
    [[crawling_items], [crawling_items], [crawling_items], [crawling_items],]
    '''
    chunks = [products[x:x + batch_size] for x in range(0, len(products), batch_size)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        executor.map(insert_data,chunks)

    return None

def get_whole_image_url_data_from_cloud():
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        query = "select image from product"
        cursor.execute(query)
        image_data = cursor.fetchall()
        conn.pool_reset_session = True

    except Exception as e:
        logging.info(f"Error : {e}")

    finally:
        if conn:
            pool.release_connection(conn)

    return image_data

def insert_data(data_chunk):
    try:
        cnx = pool.get_connection()
        cursor = cnx.cursor()

        query = "INSERT INTO product (detailHtml, detailInfo, price, image, productName, productType, shopId, shopName)" \
                " values (%(detailHtml)s, %(detailInfo)s, %(price)s, %(image)s, %(productName)s, %(productType)s, %(shopId)s, %(shopName)s)"

        cursor.executemany(query, data_chunk)
        cnx.commit()
        cnx.pool_reset_session = True # connection을 Connection Pool에 반환하기 전에 세션을 리셋합니다.
    except Exception as e:
        logging.info(f"Error : {e}")
    finally:
        if cnx: # connection을 connection pool에 반환
            pool.release_connection(cnx)


# 데이터 중복 체크 시 사용됩니다.
def check_duplicate_data(crawling_datas, db_image_datas):
    key = 'image'
    result = [crawling_data for crawling_data in crawling_datas
              if not any(crawling_data[key] == db_image_data[key] for db_image_data in db_image_datas)]
    return [list(element.values()) for element in result]
