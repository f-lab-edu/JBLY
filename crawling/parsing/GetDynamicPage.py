from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def getTotalItemList():
    # WebDriver를 초기화합니다.
    driver = webdriver.Chrome()

    # 웹 페이지를 로드합니다.
    # driver.get("https://m.more-cherry.com/category/outwear/24")
    driver.get("https://m.more-cherry.com/product/list_thumb.html?cate_no=42")
    element = driver.find_element(by=By.XPATH, value='//*[@id="contents"]/div[4]/a')

    currentPage = driver.find_element(by=By.XPATH, value='//*[@id="more_current_page"]')
    print("current page is = ", currentPage.text)

    totalPage = driver.find_element(by=By.XPATH, value='//*[@id="more_total_page"]')
    print("total page is = ", totalPage.text)

    loopingTime = int(totalPage.text) - int(currentPage.text)
    storeName = "morecherry"
    itemType = "shoes"
    for i in range(loopingTime):
        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # div.xans-element-.xans-product.xans-product-listnormal.ec-base-product.typeThumb > ul"
    # datas = soup.find_all("ul", "prdList grid2")  # 상품이 담겨있는 부분의 리스트를 가져옵니다.
    datas = soup.find("ul", "prdList grid2").find_all("li", recursive=False)
    datas = list(map(str, datas))  # 문자열로 변경 후
    # datas = datas.split('<li class="xans-record-">')  # 각 상품마다 담기는 리스트로 만듭니다.
    datas = datas[1:]
    print("datas = ", len(datas))

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

    driver.close()

