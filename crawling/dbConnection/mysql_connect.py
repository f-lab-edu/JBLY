from dbConnection import cloud_db_connection_Info
# from dbConnection import MysqlConnectionInfo
# todo 책임 분리
def connect():
    # productsData order = storeName, itemName, imageUrl, price, itemType, detailInfo, shopId, detailHtml
    connector = cloud_db_connection_Info.connector()
    return connector

def disconnect(connector):
    connector.close()
    return None
