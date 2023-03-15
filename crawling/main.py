from parsing import MoreCherrySiteCrawling, PorternaSiteCrawling, TheVerlinSiteCrawling, WebExecutor
from dbConnection import MysqlConnect, ProductQuery
import datetime

if __name__ == '__main__':
    # dataTypes = storeName, itemName, imageUrl, price, itemType, detailInfo shopId

    driver = WebExecutor.executor()

    beforeCrawling = datetime.datetime.now()
    beforeCrawlingTime = beforeCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print(beforeCrawlingTime)

    # shopId == 1
    porternaProducts = PorternaSiteCrawling.getTotalProducts(driver)
    ProductQuery.insertProductIsNotExist(porternaProducts)

    # shopId == 2
    moreCherryProducts = MoreCherrySiteCrawling.getTotalProducts(driver)
    ProductQuery.insertProductIsNotExist(moreCherryProducts)

    # shopId == 3
    theverlinProducts = TheVerlinSiteCrawling.getTotalItemList(driver)
    ProductQuery.insertProductIsNotExist(theverlinProducts)

    afterCrawling = datetime.datetime.now()
    afterCrawlingTime = afterCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print(afterCrawlingTime)

    driver.close()
