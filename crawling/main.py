import datetime
import Application
import sys
import logging

sys.setrecursionlimit(10 ** 7) # RecursionError 방지
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':

    beforeCrawling = datetime.datetime.now()
    beforeCrawlingTime = beforeCrawling.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Crawling Application 실행 전 시간 : {beforeCrawlingTime}")

    # Application.run()
    logging.info("Crawling Application 입니다.")

    afterCrawling = datetime.datetime.now()
    afterCrawlingTime = afterCrawling.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Crawling Application 실행 후 시간 : {afterCrawlingTime}")

