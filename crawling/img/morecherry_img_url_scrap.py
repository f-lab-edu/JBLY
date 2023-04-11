import urllib.request
from bs4 import BeautifulSoup
import requests
from common.ProductTypes import product_types
import urllib3
import ssl
from urllib.parse import quote
import logging
from href.morecherry_deatil_url_scrapy import detail_url_scraper

urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
main_url = "https://more-cherry.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
find_key = '<div class="xans-element- xans-product xans-product-additional ">'


def morecherry_img_url_scrper(target_url):
    etc_img_tag_list = []
    clothes_img_tag_list = []
    href_list = detail_url_scraper(target_url)
    for href in href_list:
        detail_url = main_url + quote(str(href))
        detail_header = {
            'Referrer': detail_url,
            'user-agent': user_agent
        }
        detail_response = requests.get(detail_url, headers=detail_header)
        if find_key in detail_response.text:
            b_soup = BeautifulSoup(detail_response.text, 'html.parser')
            detail_html = b_soup.find(id="prdDetail")
            try:
                etc_img_tag_list = etc_img_tag_list.append(detail_html.find_all("img")[0])
                clothes_img_tag_list = clothes_img_tag_list.append(detail_html.find_all("img")[-1])
            except IndexError as e:
                logging.info(e, "img 태그가 존재하지 않습니다.")
    return None
