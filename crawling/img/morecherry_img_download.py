import re
import urllib.request
from bs4 import BeautifulSoup
import requests
from common.ProductTypes import product_types
import urllib3
import ssl
import hashlib
from img import img_crop
from img_crop import img_cropper
from urllib.parse import quote
import numpy as np
import cv2
from img.etc_img_crop import etc_img_cropper

urllib3.disable_warnings()

ssl._create_default_https_context = ssl._create_unverified_context

main_url = "https://more-cherry.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
find_key = '<ul class="prdList grid4">'

def find_last_page(target_url):
    page_num = 1
    header = {
        'Referrer': target_url + str(page_num),
        'user-agent': user_agent
    }
    response = requests.get(target_url + str(page_num), headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    find_ul = str(soup.find('a', 'last'))
    match = re.search(r'\?page=(\d+)', find_ul)
    page_num = int(match.group(1))
    return page_num


def detail_url_scraper(target_url):
    href_list = []
    for page_num in range(1, find_last_page(target_url) + 1):
        header = {
            'Referrer': target_url + str(page_num),
            'user-agent': user_agent
        }
        response = requests.get(target_url + str(page_num), headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.find_all('ul', {'class': 'prdList grid4'})
        href_set = set()
        for ul_tag in soup:
            a_tags = ul_tag.find_all('a')
            for a_tag in a_tags:
                href = a_tag.get('href')
                if href is not None:
                    href_set.add(href)
        href_list += list(href_set)
    return href_list


def morecherry_img_downloader(target_url, item_type):
    href_list = detail_url_scraper(target_url)
    for href in href_list:
        detail_url = main_url + quote(str(href))
        detail_header = {
            'Referrer': detail_url,
            'user-agent': user_agent
        }
        detail_response = requests.get(detail_url, headers=detail_header)
        if find_key not in detail_response.text:
            pass
        else:
            b_soup = BeautifulSoup(detail_response.text, 'html.parser')
            detail_html = b_soup.find(id="prdDetail")
            etc_img_tag = detail_html.find_all("img")[0]
            clothes_img_tag = detail_html.find_all("img")[-1]

            if item_type == product_types.OUTWEAR.name or item_type == product_types.TOP.name or item_type == product_types.BOTTOM.name:
                img_url = main_url + clothes_img_tag['ec-data-src']
                with urllib.request.urlopen(img_url) as response:
                    data = response.read()
                    img = np.asarray(bytearray(data), dtype=np.uint8)
                    img_cropper(img, item_type)
            else:
                img_url = main_url + etc_img_tag['ec-data-src']
                with urllib.request.urlopen(img_url) as response:
                    data = response.read()
                    img = np.asarray(bytearray(data), dtype=np.uint8)
                    etc_img_cropper(img, item_type)

    return None
