import requests
import threading
from collections import defaultdict

the_verlin_total_url = defaultdict(list)
threads = []

baseUrl = "https://theverlin.com/"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': baseUrl,
    'user-agent': user_agent
}

urls = [
    "https://theverlin.com/product/list.html?cate_no=42&page=",
    "https://theverlin.com/product/list.html?cate_no=43&page=",
    "https://theverlin.com/product/list.html?cate_no=44&page=",
    "https://theverlin.com/product/list.html?cate_no=48&page=",
    "https://theverlin.com/category/shoes/193/?page=",
]
find_key = 'class="item xans-record-">'
store_name = "theverlin"


def fetch_url(url, the_verlin_total_url):
    startPoint = 1

    while True:
        temp_url = url + str(startPoint)
        response = requests.get(temp_url, headers=header)
        startPoint += 1
        if find_key in response.text:
            the_verlin_total_url[store_name].append(temp_url)
        else:
            break


def gatherUrls():
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, the_verlin_total_url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return the_verlin_total_url
