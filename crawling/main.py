from parsing import MoreCherrySiteCrawling, PorternaSiteCrawling, TheVerlinSiteCrawling
from dbConnection import MysqlConnect, ProductQuery
import datetime

if __name__ == '__main__':
    # dataTypes = storeName, itemName, imageUrl, price, itemType, detailInfo shopId

    connectDB = MysqlConnect.connect()

    beforeCrawling = datetime.datetime.now()
    beforeCrawlingTime = beforeCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print(beforeCrawlingTime)

    # shopId == 1
    porternaProducts = PorternaSiteCrawling.getTotalProducts()
    porternaInsertData = ProductQuery.checkDuplicatedProducts(connectDB, porternaProducts)
    ProductQuery.insertProducts(connectDB, porternaInsertData)

    # shopId == 2
    moreCherryProducts = MoreCherrySiteCrawling.getTotalProducts()
    moreCherryInsertData = ProductQuery.checkDuplicatedProducts(connectDB, moreCherryProducts)
    ProductQuery.insertProducts(connectDB, moreCherryInsertData)

    # shopId == 3
    theverlinProducts = TheVerlinSiteCrawling.getTotalItemList()
    theverlinInsertData = ProductQuery.checkDuplicatedProducts(connectDB, theverlinProducts)
    ProductQuery.insertProducts(connectDB, theverlinInsertData)

    afterCrawling = datetime.datetime.now()
    afterCrawlingTime = afterCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print(afterCrawlingTime)

    MysqlConnect.disconnect(connectDB)  # DB disconnect
