import requests
import threading
from collections import defaultdict
from crawlingSite.ProductTypes import productTypes

baseUrl = "https://theverlin.com/"
crawling_file_name = "TheVerlinSiteCrawling"
find_key = 'class="item xans-record-">'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': baseUrl,
    'user-agent': user_agent
}
the_verlin_total_url = defaultdict(list)
urls = [
    ("https://theverlin.com/product/list.html?cate_no=42&page=", productTypes.OUTWEAR.name),
    ("https://theverlin.com/product/list.html?cate_no=43&page=", productTypes.TOP.name),
    ("https://theverlin.com/product/list.html?cate_no=44&page=", productTypes.BOTTOM.name),
    ("https://theverlin.com/product/list.html?cate_no=48&page=", productTypes.ACCESSORY.name),
    ("https://theverlin.com/category/shoes/193/?page=", productTypes.SHOES.name),
]
threads = []

def fetch_url(url, item_type, the_verlin_total_url):
    startPoint = 1

    while True:
        temp_url = url + str(startPoint)
        response = requests.get(temp_url, headers=header)
        startPoint += 1
        if find_key in response.text:
            the_verlin_total_url[crawling_file_name].append((response, item_type))
        else:
            break


def gather_urls():
    for each_url in urls:
        url, item_type = each_url
        thread = threading.Thread(target=fetch_url, args=(url, item_type, the_verlin_total_url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return the_verlin_total_url
