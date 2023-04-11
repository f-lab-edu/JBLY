import requests
import concurrent.futures
from common.ProductTypes import product_types

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
base_url = "https://theverlin.com/"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}
the_verlin_total_url = []


def fetch_url(url):
    crawling_module_name = "TheVerlinSiteCrawling"
    find_key = 'class="item xans-record-">'

    each_url, product_type = url
    page_number = 1

    while True:
        temp_url = each_url + str(page_number)
        response = requests.get(temp_url, headers=header)
        page_number += 1
        if find_key in response.text:
            the_verlin_total_url.append([crawling_module_name, response, product_type])
        else:
            break


def gather_urls():
    shop_name = "theverlin"

    urls = [
        ("https://theverlin.com/product/list.html?cate_no=42&page=", product_types.OUTWEAR.name),
        ("https://theverlin.com/product/list.html?cate_no=43&page=", product_types.TOP.name),
        ("https://theverlin.com/product/list.html?cate_no=44&page=", product_types.BOTTOM.name),
        ("https://theverlin.com/product/list.html?cate_no=48&page=", product_types.ACCESSORY.name),
        ("https://theverlin.com/category/shoes/193/?page=", product_types.SHOES.name),
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(fetch_url, urls)

    return [the_verlin_total_url, base_url, user_agent, shop_name]
