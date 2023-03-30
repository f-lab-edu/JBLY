import re
import urllib.request
from bs4 import BeautifulSoup
import requests
from common.ProductTypes import product_types
import urllib3
import ssl
import hashlib

urllib3.disable_warnings()

ssl._create_default_https_context = ssl._create_unverified_context

path_folder_outwear = 'D:\\Jblyoutwear\\'
path_folder_top = 'D:\\Jblytop\\'
path_folder_bottom = 'D:\\Jblybottom\\'
path_folder_acc = 'D:\\Jblyacc\\'
path_folder_shoes = 'D:\\Jblyshoes\\'

main_url = "https://theverlin.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"


def find_last_page(target_url):
    page_num = 1
    pattern = r'<li.*?>.*?<em>(\d+)</em>.*?</li>'
    header = {
        'Referrer': main_url,
        'user-agent': user_agent
    }
    response = requests.get(target_url+str(page_num), headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    find_li = soup.find('div', 'xans-element- xans-product xans-product-normalpaging')
    find_li = find_li.find_all('li')
    find_li = list(map(str, find_li))
    string = str(find_li[-1])
    match = re.search(pattern, string)
    number = match.group(1)
    return number

def detail_url_scraper(target_url):
    for page_num in range(1, int(find_last_page(target_url)) + 1):
        header = {
            'Referrer': target_url + str(page_num),
            'user-agent': user_agent
        }
        response = requests.get(target_url + str(page_num), headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.find_all('ul', {'class': 'prdList column4'})
        href_set = set()
        for ul_tag in soup:
            a_tags = ul_tag.find_all('a')
            for a_tag in a_tags:
                href = a_tag.get('href')
                if href is not None:
                    href_set.add(href)
        href_list = list(href_set)
        return href_list


def theverlin_img_downloader(target_url, item_type):
    href_list = detail_url_scraper(target_url)
    for href in href_list:
        detail_url = main_url + str(href)
        detail_header = {
            'Referrer': detail_url,
            'user-agent': user_agent
        }
        detail_response = requests.get(detail_url, headers=detail_header)
        b_soup = BeautifulSoup(detail_response.text, 'html.parser')
        detail_html = b_soup.find("div", "edibot-product-detail").find_all("img")


        link_img = []
        for img in detail_html:
            link_img.append("https://theverlin.com" + img['ec-data-src'])
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
        return None
