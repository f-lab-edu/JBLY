from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def getTotalProducts():
    driver = webdriver.Chrome()

    storeName = "porterna"
    result = [] # storeName, itemName, getUrl, getPrice, itemType
    urls = []

    # outwear
    urls.append("https://porterna.com/product/list.html?cate_no=541")

    # top
    urls.append("https://porterna.com/product/list.html?cate_no=789")

    # pants
    urls.append("https://porterna.com/product/list.html?cate_no=28")

    # acc
    urls.append("https://porterna.com/product/list.html?cate_no=44")

    # shoes
    urls.append("https://porterna.com/product/list.html?cate_no=79")

    url = urls[0]

    itemType = "outwear"

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    datas = soup.find("ul", "thumbnail").find_all("li", recursive=False)
    datas = list(map(str, datas))
    print(datas[0])
    print("datas = ", len(datas))
    eachData = BeautifulSoup(datas[0], 'html.parser')
    # find = eachData.find('img', {'class': 'thumb-img'})

    find = eachData.find('img')
    getImageUrl = find['src']
    imageUrl = 'https:' + getImageUrl

    getItemName = eachData.find('p', {'class': 'name'})
    itemName = getItemName.text

    getPrice = eachData.find('div', {'class': 'price1'})
    price = getPrice.text

    print(storeName, itemName, imageUrl, price, itemType)
    return None
