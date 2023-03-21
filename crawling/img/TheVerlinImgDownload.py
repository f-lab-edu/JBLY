import os.path
import re
import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import requests
import uuid
from parsing.ProductTypes import productTypes
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

urls = []
urls.append(("https://theverlin.com/product/list.html?cate_no=42&page=", productTypes.OUTWEAR.name))  # outwear
urls.append(("https://theverlin.com/product/list.html?cate_no=43&page=", productTypes.TOP.name))  # top
urls.append(("https://theverlin.com/product/list.html?cate_no=44&page=", productTypes.BOTTOM.name))  # bottom
urls.append(("https://theverlin.com/product/list.html?cate_no=48&page=", productTypes.ACCESSORY.name))  # acc
urls.append(("https://theverlin.com/product/list.html?cate_no=193&page=", productTypes.SHOES.name))  # shoes

main_url = "https://theverlin.com/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
detail_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

for url in urls:
    page_num = 1
    each_url, itemType = url

    while True:
        header = {
            'Referrer': each_url + str(page_num),
            'user-agent': user_agent
        }
        page_num += 1
        response = requests.get(each_url + str(page_num), headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')

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
                    if itemType == productTypes.OUTWEAR.name:
                        with urllib.request.urlopen(link) as response:
                            data = response.read()
                            md5hash = hashlib.md5(data).hexdigest()
                            md5hash = md5hash + ".jpg"
                            with open(path_folder_outwear + md5hash, 'wb') as f:
                                f.write(data)

                    elif itemType == productTypes.TOP.name:
                        with urllib.request.urlopen(link) as response:
                            data = response.read()
                            md5hash = hashlib.md5(data).hexdigest()
                            md5hash = md5hash + ".jpg"
                            with open(path_folder_top + md5hash, 'wb') as f:
                                f.write(data)

                    elif itemType == productTypes.BOTTOM.name:
                        with urllib.request.urlopen(link) as response:
                            data = response.read()
                            md5hash = hashlib.md5(data).hexdigest()
                            md5hash = md5hash + ".jpg"
                            with open(path_folder_bottom + md5hash, 'wb') as f:
                                f.write(data)

                    elif itemType == productTypes.ACCESSORY.name:
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
