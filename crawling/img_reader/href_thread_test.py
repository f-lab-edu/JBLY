import os.path
import re
import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import requests
import urllib.request as req
import os
import concurrent.futures
import threading
import time

main_url = "https://porterna.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"


def find_last_page(target_url):
    pattern = r'<li class="xans-record-"><a class="other" href="\?cate_no=\d+&amp;page=(\d+)">'
    header = {
        'Referrer': main_url,
        'user-agent': user_agent
    }

    response = requests.get(target_url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    find_li = soup.find('div', 'xans-element- xans-product xans-product-normalpaging paging')
    find_li = find_li.find_all('li')
    find_li = list(map(str, find_li))
    string = str(find_li[-1])
    match = re.search(pattern, string)
    number = match.group(1)
    return number


def detail_url_scraper(target_url, page_num):
    href_set = set()
    header = {
        'Referrer': target_url + str(page_num),
        'user-agent': user_agent
    }
    response = requests.get(target_url + str(page_num), headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find_all('ul', {'class': 'thumbnail'})
    for ul_tag in soup:
        a_tags = ul_tag.find_all('a')
        for a_tag in a_tags:
            href = a_tag.get('href')
            if href is not None:
                href_set.add(href)
    return href_set

if __name__ == "__main__":
    start_time = time.time()
    target_url = "https://porterna.com/product/list.html?cate_no=79&page="
    last_page = int(find_last_page(target_url))
    href_list = []
    with concurrent.futures.ThreadPoolExecutor() as executor: # 쓰레드 풀 생성
        future_to_url = {executor.submit(detail_url_scraper, target_url, page_num): page_num for page_num in range(1, last_page+1)}
        for future in concurrent.futures.as_completed(future_to_url):
            page_num = future_to_url[future]
            try:
                href_set = future.result()
                href_list += list(href_set)
            except Exception as exc:
                print(f"page_num {page_num} generated an exception: {exc}")
    print(len(href_list))
    print(f"{time.time() - start_time} sec")
