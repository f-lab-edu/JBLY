import os.path
import re
import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import requests
import uuid
from parsing.ProductTypes import product_types
import urllib3
import ssl
import urllib.request as req
import json
import os
from datetime import datetime
import hashlib

urllib3.disable_warnings()

ssl._create_default_https_context = ssl._create_unverified_context

path_folder_outwear = 'D:\\Jblyoutwear\\'
path_folder_outer = 'D:\\Jblyouter\\'
path_folder_top = 'D:\\Jblytop\\'
path_folder_bottom = 'D:\\Jblybottom\\'
path_folder_acc = 'D:\\Jblyacc\\'
path_folder_shoes = 'D:\\Jblyshoes\\'

main_url = "https://theverlin.com/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
detail_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"


def theverlin_img_downloader(target_url, item_type):
    page_num = 1
    while True:
        header = {
            'Referrer': target_url + str(page_num),
            'user-agent': user_agent
        }
        response = requests.get(target_url + str(page_num), headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_num += 1

        try:
            datas = soup.find('ul', 'prdList column4').find_all("li", recursive=False)
            datas = list(map(str, datas))
        except:
            break

        for data in datas:
            each_data = BeautifulSoup(data, 'html.parser')
            get_detail_info = each_data.find('a')['href']
            detail_info = main_url + get_detail_info

            detail_header = {
                'Referrer': detail_info,
                'user-agent': detail_user_agent
            }
            detail_response = requests.get(detail_info, headers=detail_header)
            bSoup = BeautifulSoup(detail_response.text, 'html.parser')

            detail_html = bSoup.find("div", "edibot-product-detail").find_all("img")

            link_img = []
            for img in detail_html:
                link_img.append("https://theverlin.com/" + img['ec-data-src'])
                for link in link_img:
                    if item_type == product_types.OUTWEAR.name:
                        with urllib.request.urlopen(link) as response:
                            data = response.read()
                            md5hash = hashlib.md5(data).hexdigest()
                            md5hash = md5hash + ".jpg"
                            with open(path_folder_outwear + md5hash, 'wb') as f:
                                f.write(data)

                    elif item_type == product_types.TOP.name:
                        with urllib.request.urlopen(link) as response:
                            data = response.read()
                            md5hash = hashlib.md5(data).hexdigest()
                            md5hash = md5hash + ".jpg"
                            with open(path_folder_top + md5hash, 'wb') as f:
                                f.write(data)

                    elif item_type == product_types.BOTTOM.name:
                        with urllib.request.urlopen(link) as response:
                            data = response.read()
                            md5hash = hashlib.md5(data).hexdigest()
                            md5hash = md5hash + ".jpg"
                            with open(path_folder_bottom + md5hash, 'wb') as f:
                                f.write(data)

                    elif item_type == product_types.ACCESSORY.name:
                        with urllib.request.urlopen(link) as response:
                            data = response.read()
                            md5hash = hashlib.md5(data).hexdigest()
                            md5hash = md5hash + ".jpg"
                            with open(path_folder_acc + md5hash, 'wb') as f:
                                f.write(data)

                    else:
                        with urllib.request.urlopen(link) as response:
                            data = response.read()
                            md5hash = hashlib.md5(data).hexdigest()
                            md5hash = md5hash + ".jpg"
                            with open(path_folder_shoes + md5hash, 'wb') as f:
                                f.write(data)
            break

