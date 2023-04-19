import datetime
import Application
import sys
import logging
from dbConnection import database_module

sys.setrecursionlimit(10 ** 7) # RecursionError 방지
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':

    beforeCrawling = datetime.datetime.now()
    beforeCrawlingTime = beforeCrawling.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"크롤링 애플리케이션 시작 시간 : {beforeCrawlingTime}")

    # Application.run()
    database_module.run()

    afterCrawling = datetime.datetime.now()
    afterCrawlingTime = afterCrawling.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"크롤링 애플리케이션 시작 시간 : {afterCrawlingTime}")

