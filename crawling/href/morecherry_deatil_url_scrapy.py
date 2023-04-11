import os
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
import urllib3
import ssl
from common.ProductTypes import product_types
import re

urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
main_url = "https://more-cherry.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
find_key = '<div class="xans-element- xans-product xans-product-additional ">'
header = {
    'Referrer': main_url,
    'user-agent': user_agent
}

def find_last_page(target_url):
    page_num = 1
    response = requests.get(target_url + str(page_num), headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    find_ul = str(soup.find('a', 'last'))
    match = re.search(r'\?page=(\d+)', find_ul)
    page_num = int(match.group(1))
    return page_num


# 마지막 페이지까지 반복문을 돌며 상품 상세 페이지 주소를 스크래핑해 리스트로 저장합니다.
def detail_url_scraper(target_url, item_type):
    href_list = []
    for page_num in range(1, find_last_page(target_url) + 1):
        response = requests.get(main_url, headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.find_all('ul', {'class': 'prdList grid4'})
        href_set = set()
        for ul_tag in soup:
            a_tags = ul_tag.find_all('a')
            for a_tag in a_tags:
                href = a_tag.get('href')
                if href is not None:
                    href_set.add(href)
        href_list += list(href_set)
    return href_list, item_type


if __name__ == '__main__':
    urls = [
        ("https://more-cherry.com/category/outwear/24/?page=", productTypes.OUTWEAR.name),
        ("https://more-cherry.com/category/top/25/?page=", productTypes.TOP.name),
        ("https://more-cherry.com/category/pants/26/?page=", productTypes.BOTTOM.name),
        ("https://more-cherry.com/category/accessory/28/?page=", productTypes.ACCESSORY.name),
        ("https://more-cherry.com/category/shoes/42/?page=", productTypes.SHOES.name),
    ]

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(detail_url_scraper, urls)


