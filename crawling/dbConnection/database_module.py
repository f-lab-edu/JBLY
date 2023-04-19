from dbConnection import MysqlConnectionInfo, product_query
import logging

logging.basicConfig(level=logging.INFO)

'''
DB 관련 처리 작업은 이곳 database_module에서 담당합니다.
'''
def run():
    # db_image_datas = product_query.get_whole_image_url_data_from_db()
    # new_data = check_duplicate_data(crawling_datas, db_image_datas)
    # product_query.insert_crawling_data(new_data)
    products = product_query.local_db_delete_id_column()
    product_query.insert_crawling_data(products)
    return None

# 데이터 중복 체크 시 사용됩니다.
def check_duplicate_data(crawling_datas, db_image_datas):
    key = 'image'
    result = [crawling_data for crawling_data in crawling_datas
              if not any(crawling_data[key] == db_image_data[key] for db_image_data in db_image_datas)]
    return [list(element.values()) for element in result]

