import requests
import threading
from common.ProductTypes import product_types

base_url = "https://theverlin.com/"
crawling_module_name = "TheVerlinSiteCrawling"
shop_name = "theverlin"
find_key = 'class="item xans-record-">'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}
the_verlin_total_url = []
urls = [
    ("https://theverlin.com/product/list.html?cate_no=42&page=", product_types.OUTWEAR.name),
    ("https://theverlin.com/product/list.html?cate_no=43&page=", product_types.TOP.name),
    ("https://theverlin.com/product/list.html?cate_no=44&page=", product_types.BOTTOM.name),
    ("https://theverlin.com/product/list.html?cate_no=48&page=", product_types.ACCESSORY.name),
    ("https://theverlin.com/category/shoes/193/?page=", product_types.SHOES.name),
]
threads = []

def fetch_url(url, item_type):
    start_point = 1

    while True:
        temp_url = url + str(start_point)
        response = requests.get(temp_url, headers=header)
        start_point += 1
        if find_key in response.text:
            the_verlin_total_url.append([crawling_module_name, response, item_type])
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

    return [the_verlin_total_url, base_url, user_agent, shop_name]
