import requests
import threading
from common.ProductTypes import product_types

base_url = "https://porterna.com"
crawling_module_name = "PorternaSiteCrawling"
shop_name = "porterna"
find_key = 'col  col20 floatleft xans-record-'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}
porterna_total_url = []
urls = [
    ("https://porterna.com/product/list.html?cate_no=541&page=", product_types.OUTWEAR.name),
    ("https://porterna.com/product/list.html?cate_no=789&page=", product_types.TOP.name),
    ("https://porterna.com/product/list.html?cate_no=28&page=", product_types.BOTTOM.name),
    ("https://porterna.com/product/list.html?cate_no=44&page=", product_types.ACCESSORY.name),
    ("https://porterna.com/product/list.html?cate_no=79&page=", product_types.SHOES.name),
]
threads = []


def fetch_url(url, item_type):
    start_point = 1

    while True:
        temp_url = url + str(start_point)
        response = requests.get(temp_url, headers=header)
        start_point += 1
        if find_key in response.text:
            porterna_total_url.append([crawling_module_name, response, item_type])
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

    return [porterna_total_url, base_url, user_agent, shop_name]
