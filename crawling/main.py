from parsing import MoreCherrySiteCrawling, PorternaSiteCrawling, TheVerlinSiteCrawling
from dbConnection import ProductQuery
import datetime

if __name__ == '__main__':

    beforeCrawling = datetime.datetime.now()
    beforeCrawlingTime = beforeCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print(beforeCrawlingTime)

    # # shopId == 1
    # porternaProducts = PorternaSiteCrawling.getTotalProducts()
    # ProductQuery.insertProductIsNotExist(porternaProducts)
    #
    # shopId == 2
    # moreCherryProducts = MoreCherrySiteCrawling.getTotalProducts()
    # ProductQuery.insertProductIsNotExist(moreCherryProducts)
    #
    # # shopId == 3
    theverlinProducts = TheVerlinSiteCrawling.getTotalItemList()
    # ProductQuery.insertProductIsNotExist(theverlinProducts)

    afterCrawling = datetime.datetime.now()
    afterCrawlingTime = afterCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print(afterCrawlingTime)

