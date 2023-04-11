from bs4 import BeautifulSoup
import requests
import urllib3
import ssl
from urllib.parse import quote
import logging
from img_reader.opencv import img_crop
from img_reader.opencv import etc_img_crop
import io

urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
main_url = "https://more-cherry.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
find_key = '<div class="xans-element- xans-product xans-product-additional ">'


def clothes_img_reader():
    try:
        img_url = main_url + clothes_img_tag['ec-data-src']
        img_url = img_url.replace(" ", "%20")
        with urllib.request.urlopen(img_url) as response:
            data = response.read()
            buffer = io.BytesIO(data) # 이미지 데이터를 버퍼에 저장합니다.
            img = np.asarray(bytearray(buffer), dtype=np.uint8) # 이미지(binary data)를 array로 변환시킵니다.
            img_cropper(img, item_type)
    except UnicodeEncodeError as e:
        logging.info(e)
    return None


def etc_img_reader():
    try:
        etc_img_url = main_url + etc_img_tag['ec-data-src']
        etc_img_url = etc_img_url.replace(" ", "%20")
        with urllib.request.urlopen(etc_img_url) as response:
            data = response.read() # buffer 사용해서 refactoring
            buffer = io.BytesIO(data)
            img = np.asarray(bytearray(buffer), dtype=np.uint8)
            etc_img_cropper(img, item_type)
    except UnicodeEncodeError as e:
        logging.info(e)


def morecherry_img_reader(item_type):
    if item_type == product_types.ACCESSORY.name or item_type == product_types.SHOES.name:
        etc_img_reader()
    else:
        clothes_img_reader()
    return None

