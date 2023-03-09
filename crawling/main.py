from parsing import MoreCherrySiteCrawling, PorternaSiteCrawling, TheVerlinSiteCrawling, WebExecutor
from dbConnection import MysqlConnect, ProductQuery
import datetime

if __name__ == '__main__':
    # dataTypes = storeName, itemName, imageUrl, price, itemType, detailInfo shopId

    connectDB = MysqlConnect.connect()
    driver = WebExecutor.executor()
    detailDriver = WebExecutor.executor()

    # shopId == 1
    porternaProducts = PorternaSiteCrawling.getTotalProducts(driver, detailDriver)
    porternaInsertData = ProductQuery.checkDuplicatedProducts(connectDB, porternaProducts)
    ProductQuery.insertProducts(connectDB, porternaInsertData)

    # shopId == 2
    moreCherryProducts = MoreCherrySiteCrawling.getTotalProducts(driver, detailDriver)
    moreCherryInsertData = ProductQuery.checkDuplicatedProducts(connectDB, moreCherryProducts)
    ProductQuery.insertProducts(connectDB, moreCherryInsertData)

    # shopId == 3
    theverlinProducts = TheVerlinSiteCrawling.getTotalItemList(driver, detailDriver)
    theverlinInsertData = ProductQuery.checkDuplicatedProducts(connectDB, theverlinProducts)
    ProductQuery.insertProducts(connectDB, theverlinInsertData)

    now = datetime.datetime.now()
    newTime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(newTime)

    driver.close()
    detailDriver.close()
    MysqlConnect.disconnect(connectDB)  # DB disconnect
