import requests
import concurrent.futures
from common.ProductTypes import product_types

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36"
base_url = "https://more-cherry.com"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}
more_cherry_total_url = []


def fetch_url(url):
    crawling_module_name = "morecherry_site_crawling"
    find_key = '<ul class="prdList grid4">'

    each_url, product_type = url
    page_number = 1

    while True:
        temp_url = each_url + str(page_number)
        response = requests.get(temp_url, headers=header)
        page_number += 1
        if find_key in response.text:
            more_cherry_total_url.append([crawling_module_name, response, product_type])
        else:
            break


def gather_urls():
    shop_name = "morecherry"

    urls = [
        ("https://more-cherry.com/category/outwear/24/?page=", product_types.OUTWEAR.name),
        ("https://more-cherry.com/category/top/25/?page=", product_types.TOP.name),
        ("https://more-cherry.com/category/pants/26/?page=", product_types.BOTTOM.name),
        ("https://more-cherry.com/category/accessory/28/?page=", product_types.ACCESSORY.name),
        ("https://more-cherry.com/category/shoes/42/?page=", product_types.SHOES.name),
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(fetch_url, urls)

    return [more_cherry_total_url, base_url, user_agent, shop_name]
