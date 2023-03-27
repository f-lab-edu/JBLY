import requests
import threading
from collections import defaultdict
from parsing.ProductTypes import productTypes

base_url = "https://porterna.com"
store_name = "PorternaSiteCrawling"
find_key = 'col  col20 floatleft xans-record-'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}
porterna_total_url = defaultdict(list)
urls = [
    ("https://porterna.com/product/list.html?cate_no=541&page=", productTypes.OUTWEAR.name),
    ("https://porterna.com/product/list.html?cate_no=789&page=", productTypes.TOP.name),
    ("https://porterna.com/product/list.html?cate_no=28&page=", productTypes.BOTTOM.name),
    ("https://porterna.com/product/list.html?cate_no=44&page=", productTypes.ACCESSORY.name),
    ("https://porterna.com/product/list.html?cate_no=79&page=", productTypes.SHOES.name),
]
threads = []


def fetch_url(url, item_type, porterna_total_url):
    startPoint = 1

    while True:
        temp_url = url + str(startPoint)
        response = requests.get(temp_url, headers=header)
        startPoint += 1
        if find_key in response.text:
            porterna_total_url[store_name].append((response, item_type))
        else:
            break


def gatherUrls():
    for each_url in urls:
        url, item_type = each_url
        thread = threading.Thread(target=fetch_url, args=(url, item_type, porterna_total_url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return porterna_total_url
