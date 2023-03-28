import requests
import threading
from collections import defaultdict
from parsing.ProductTypes import productTypes

more_cherry_total_url = defaultdict(list)
threads = []

base_url = "https://more-cherry.com"
store_name = "MoreCherrySiteCrawling"
find_key = '<ul class="prdList grid4">'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}
more_cherry_total_url = defaultdict(list)
urls = [
    ("https://more-cherry.com/category/outwear/24/?page=", productTypes.OUTWEAR.name),
    ("https://more-cherry.com/category/top/25/?page=", productTypes.TOP.name),
    ("https://more-cherry.com/category/pants/26/?page=", productTypes.BOTTOM.name),
    ("https://more-cherry.com/category/accessory/28/?page=", productTypes.ACCESSORY.name),
    ("https://more-cherry.com/category/shoes/42/?page=", productTypes.SHOES.name),
]
threads = []


def fetch_url(url, item_type, more_cherry_total_url):
    startPoint = 1

    while True:
        temp_url = url + str(startPoint)
        response = requests.get(temp_url, headers=header)
        startPoint += 1
        if find_key in response.text:
            more_cherry_total_url[store_name].append((response, item_type))
        else:
            break


def gather_urls():
    for each_url in urls:
        url, item_type = each_url
        thread = threading.Thread(target=fetch_url, args=(url, item_type, more_cherry_total_url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return more_cherry_total_url
