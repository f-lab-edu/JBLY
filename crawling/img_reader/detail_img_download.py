import requests
import threading
from collections import defaultdict
from parsing.ProductTypes import productTypes

more_cherry_total_url = defaultdict(list)
threads = []

base_url = "https://more-cherry.com"
find_key = '<ul class="prdList grid4">'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
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

def mc_img_downloader(url, item_type, more_cherry_total_url):
    return None



# def fetch_url(url, item_type, more_cherry_total_url):
#     for
#     if find_key in response.text:
#         more_cherry_total_url[crawling_file_name].append((response, item_type))
#     else:
#         break
