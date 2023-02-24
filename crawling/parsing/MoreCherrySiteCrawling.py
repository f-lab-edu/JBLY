from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import re # regex

ssl._create_default_https_context = ssl._create_unverified_context

def getDatas():
    urls = []
    result = []
    sequence = 0
    storeName = "morecherry" # 5개의 필드
    urls.append("https://m.more-cherry.com/category/outwear/24") # outwear
    urls.append("https://m.more-cherry.com/category/top/25/") # top
    urls.append("https://m.more-cherry.com/category/pants/26/") # pants
    urls.append("https://m.more-cherry.com/category/accessory/28/") # acc
    urls.append("https://m.more-cherry.com/product/list_thumb.html?cate_no=42") # shoes

    splitedUrl = urls[0].split("/")
    itemType = splitedUrl[-2]
    html = urlopen(urls[0])
    soup = BeautifulSoup(html, 'html.parser')

    datas = soup.find_all("ul", "prdList grid2") # 상품이 담겨있는 부분의 리스트를 가져옵니다.
    datas = str(datas) # 문자열로 변경 후
    datas = datas.split('<li class="xans-record-">') # 각 상품마다 담기는 리스트로 만듭니다.
    datas = datas[1:]

    for data in datas:
        targetData = BeautifulSoup(data, 'html.parser')
        # get Item
        itemTag = targetData.find('span', {'class': 'name'})
        itemName = itemTag.text

        # get Image
        imageTag = targetData.find('img')
        url = imageTag['src']
        getUrl = 'https:' + url


        # get Price
        priceTag = targetData.find('li', {'class': 'price'})
        getPrice = priceTag.text.replace(',', '')
        getPrice = getPrice.replace('원','')

        print(storeName, itemName, getUrl, getPrice, itemType)
        print("============================================================")
    return None