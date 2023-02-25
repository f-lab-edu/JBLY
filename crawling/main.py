from parsing import MoreCherrySiteCrawling
from parsing import PorternaSiteCrawling
from dbConnection import MysqlConnect
if __name__ == '__main__':
    # dataTypes = storeName, itemName, imageUrl, price, itemType shopId
    results = []

    # shopId == 1
    porternaProducts = PorternaSiteCrawling.getTotalProducts()

    # shopId == 2
    moreCherryProducts = MoreCherrySiteCrawling.getTotalProducts()

    # shopId == 3
    # theverlinProducts = TheVerlinSiteCrawling.getTotalProducts()

    results.extend(porternaProducts)
    results.extend(moreCherryProducts)
    # results.extend(theverlinProducts)

    MysqlConnect.connect(results)