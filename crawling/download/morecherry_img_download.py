from href.morecherry_deatil_url_scrapy import detail_url_scraper
from img.morecherry_img_url_scrap import morecherry_img_url_scrper

def morecherry_img_downloader(target_url, item_type):
    detail_url_scraper(target_url)
    morecherry_img_url_scrper(detail_url_scraper)
    