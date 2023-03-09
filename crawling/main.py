from parsing import MoreCherrySiteCrawling, PorternaSiteCrawling, TheVerlinSiteCrawling, WebExecutor
from dbConnection import MysqlConnect, ProductQuery
import datetime

if __name__ == '__main__':
    # dataTypes = storeName, itemName, imageUrl, price, itemType, detailInfo shopId

    connectDB = MysqlConnect.connect()

    # shopId == 1
    # porternaProducts = PorternaSiteCrawling.getTotalProducts()
    # print("4")
    # porternaInsertData = ProductQuery.checkDuplicatedProducts(connectDB, porternaProducts)
    # print("5")
    # ProductQuery.insertProducts(connectDB, porternaInsertData)
    # print("6")
    # shopId == 2
    moreCherryProducts = MoreCherrySiteCrawling.getTotalProducts()
    moreCherryInsertData = ProductQuery.checkDuplicatedProducts(connectDB, moreCherryProducts)
    ProductQuery.insertProducts(connectDB, moreCherryInsertData)

    # shopId == 3
    # theverlinProducts = TheVerlinSiteCrawling.getTotalItemList(driver, detailDriver)
    # theverlinInsertData = ProductQuery.checkDuplicatedProducts(connectDB, theverlinProducts)
    # ProductQuery.insertProducts(connectDB, theverlinInsertData)

    now = datetime.datetime.now()
    newTime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(newTime)

    MysqlConnect.disconnect(connectDB)  # DB disconnect
