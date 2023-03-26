import requests
import threading
from collections import defaultdict

more_cherry_total_url = defaultdict(list)
threads = []

base_url = "https://more-cherry.com"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}

urls = [
    "https://more-cherry.com/category/outwear/24/?page=",
    "https://more-cherry.com/category/top/25/?page=",
    "https://more-cherry.com/category/pants/26/?page=",
    "https://more-cherry.com/category/accessory/28/?page=",
    "https://more-cherry.com/category/shoes/42/?page=",
]
find_key = '<ul class="prdList grid4">'
store_name = "more-cherry"


def fetch_url(url, more_cherry_total_url):
    startPoint = 1

    while True:
        temp_url = url + str(startPoint)
        response = requests.get(temp_url, headers=header)
        startPoint += 1
        if find_key in response.text:
            more_cherry_total_url[store_name].append(temp_url)
        else:
            break


def gatherUrls():
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, more_cherry_total_url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return more_cherry_total_url
