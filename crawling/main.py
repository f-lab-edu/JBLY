from parsing import MoreCherrySiteCrawling, PorternaSiteCrawling, TheVerlinSiteCrawling
from dbConnection import MysqlConnect
from dbConnection import ProductQuery
import datetime

if __name__ == '__main__':
    # dataTypes = storeName, itemName, imageUrl, price, itemType, detailInfo shopId

    connectDB = MysqlConnect.connect()

    # shopId == 1
    porternaProducts = PorternaSiteCrawling.getTotalProducts()
    porternaInsertData = ProductQuery.checkDuplicatedProducts(connectDB, porternaProducts)
    ProductQuery.insertProducts(connectDB, porternaInsertData)

    # # shopId == 2
    # moreCherryProducts = MoreCherrySiteCrawling.getTotalProducts()
    # moreCherryInsertData = ProductQuery.checkDuplicatedProducts(connectDB, moreCherryProducts)
    # ProductQuery.insertProducts(connectDB, moreCherryInsertData)

    # # shopId == 3
    # theverlinProducts = TheVerlinSiteCrawling.getTotalItemList()
    # theverlinInsertData = ProductQuery.checkDuplicatedProducts(connectDB, theverlinProducts)
    # ProductQuery.insertProducts(connectDB, theverlinInsertData)

    now = datetime.datetime.now()
    newTime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(newTime)

    MysqlConnect.disconnect(connectDB)  # DB disconnect
