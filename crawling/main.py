# from dbConnection import ProductQuery
from urlCollection import UrlCollectionModule
from util import Chunker
from crawlingSite import CrawlingSiteModule
import datetime

if __name__ == '__main__':

    beforeCrawling = datetime.datetime.now()
    beforeCrawlingTime = beforeCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print(beforeCrawlingTime)

    urls = UrlCollectionModule.url_collecting()
    chunked_urls = Chunker.url_chunk(urls)

    results = CrawlingSiteModule.crawling_each_site(chunked_urls)
    for result in results:
        print(len(result))


    afterCrawling = datetime.datetime.now()
    afterCrawlingTime = afterCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print(afterCrawlingTime)

