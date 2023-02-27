from crawling.parsing import MoreCherrySiteCrawling, PorternaSiteCrawling
from parsing import TheVerlinSiteCrawling
from dbConnection import MysqlConnect
if __name__ == '__main__':
    # dataTypes = storeName, itemName, imageUrl, price, itemType shopId
    results = []

    # shopId == 1
    # porternaProducts = PorternaSiteCrawling.getTotalProducts()
    # MysqlConnect.connect(porternaProducts)
    #
    # # shopId == 2
    # moreCherryProducts = MoreCherrySiteCrawling.getTotalProducts()
    # MysqlConnect.connect(moreCherryProducts)

    # shopId == 3
    theverlinProducts = TheVerlinSiteCrawling.getTotalItemList()
    MysqlConnect.connect(theverlinProducts)



