import requests
import threading
from common.ProductTypes import product_types

base_url = "https://more-cherry.com"
crawling_module_name = "MoreCherrySiteCrawling"
shop_name = "morecherry"
find_key = '<ul class="prdList grid4">'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}
more_cherry_total_url = []
urls = [
    ("https://more-cherry.com/category/outwear/24/?page=", product_types.OUTWEAR.name),
    ("https://more-cherry.com/category/top/25/?page=", product_types.TOP.name),
    ("https://more-cherry.com/category/pants/26/?page=", product_types.BOTTOM.name),
    ("https://more-cherry.com/category/accessory/28/?page=", product_types.ACCESSORY.name),
    ("https://more-cherry.com/category/shoes/42/?page=", product_types.SHOES.name),
]
threads = []


def fetch_url(url, item_type):
    page_number = 1

    while True:
        temp_url = url + str(page_number)
        response = requests.get(temp_url, headers=header)
        page_number += 1
        if find_key in response.text:
            more_cherry_total_url.append([crawling_module_name, response, item_type])
        else:
            break

def gather_urls():
    for each_url in urls:
        url, item_type = each_url
        thread = threading.Thread(target=fetch_url, args=(url, item_type))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return [more_cherry_total_url, base_url, user_agent, shop_name]