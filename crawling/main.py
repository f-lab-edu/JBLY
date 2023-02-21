from dbConnection import MysqlConnect
from parsing import YTNNewPageCrawling
if __name__ == '__main__':
    MysqlConnect.connect()
    YTNNewPageCrawling.parsingData()
