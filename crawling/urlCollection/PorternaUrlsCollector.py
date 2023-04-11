import concurrent.futures
import requests
from common.ProductTypes import product_types

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
base_url = "https://porterna.com"
header = {
    'Referrer': base_url,
    'user-agent': user_agent
}
porterna_total_url = []


def fetch_url(url):
    crawling_module_name = "PorternaSiteCrawling"
    find_key = 'col  col20 floatleft xans-record-'

    each_url, product_type = url
    page_number = 1

    while True:
        temp_url = each_url + str(page_number)
        response = requests.get(temp_url, headers=header)
        page_number += 1
        if find_key in response.text:
            porterna_total_url.append([crawling_module_name, response, product_type])
        else:
            break


def gather_urls():
    shop_name = "porterna"

    urls = [
        ("https://porterna.com/product/list.html?cate_no=541&page=", product_types.OUTWEAR.name),
        ("https://porterna.com/product/list.html?cate_no=789&page=", product_types.TOP.name),
        ("https://porterna.com/product/list.html?cate_no=28&page=", product_types.BOTTOM.name),
        ("https://porterna.com/product/list.html?cate_no=44&page=", product_types.ACCESSORY.name),
        ("https://porterna.com/product/list.html?cate_no=79&page=", product_types.SHOES.name),
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(fetch_url, urls)

    return [porterna_total_url, base_url, user_agent, shop_name]
