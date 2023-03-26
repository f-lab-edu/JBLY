import requests
import threading
from collections import defaultdict

porterna_total_url = defaultdict(list)
threads = []

base_url = "https://porterna.com"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}

urls = [
    "https://porterna.com/product/list.html?cate_no=541&page=",
    "https://porterna.com/product/list.html?cate_no=789&page=",
    "https://porterna.com/product/list.html?cate_no=28&page=",
    "https://porterna.com/product/list.html?cate_no=44&page=",
    "https://porterna.com/product/list.html?cate_no=79&page=",
]
find_key = 'col  col20 floatleft xans-record-'
store_name = "porterna"


def fetch_url(url, porterna_total_url):
    startPoint = 1

    while True:
        temp_url = url + str(startPoint)
        response = requests.get(temp_url, headers=header)
        startPoint += 1
        if find_key in response.text:
            porterna_total_url[store_name].append(temp_url)
        else:
            break


def gatherUrls():
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, porterna_total_url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return porterna_total_url
