from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def getTotalItemList():
    # WebDriver를 초기화합니다.
    driver = webdriver.Chrome()

    # Var Setting
    storeName = "morecherry"
    result = []
    urls = []
    urls.append("https://m.more-cherry.com/category/outwear/24")  # outwear
    urls.append("https://m.more-cherry.com/category/top/25")  # top
    urls.append("https://m.more-cherry.com/category/pants/26")  # pants
    urls.append("https://m.more-cherry.com/category/accessory/28")  # acc
    urls.append("https://m.more-cherry.com/product/list_thumb.html?cate_no=42")  # shoes

    for url in urls:
        itemType = ""
        if "category" in url:
            splitedUrl = url.split("/")
            itemType = splitedUrl[-2]
        else:
            itemType = "shoes"
        # 웹 페이지를 로드합니다.
        driver.get(url)
        element = driver.find_element(by=By.XPATH, value='//*[@id="contents"]/div[4]/a')

        # Get Total Page
        currentPage = driver.find_element(by=By.XPATH, value='//*[@id="more_current_page"]')
        totalPage = driver.find_element(by=By.XPATH, value='//*[@id="more_total_page"]')

        loopingTime = int(totalPage.text) - int(currentPage.text)

        for i in range(1):
            driver.execute_script("arguments[0].click();", element)
            time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        datas = soup.find("ul", "prdList grid2").find_all("li", recursive=False)
        datas = list(map(str, datas))  # 문자열로 변경 후
        datas = datas[1:]
        print("datas = ", len(datas))

        for data in datas:
            itemInfoGather = []
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

            itemInfoGather.append(storeName)
            itemInfoGather.append(itemName)
            itemInfoGather.append(getUrl)
            itemInfoGather.append(getPrice)
            itemInfoGather.append(itemType)
            copyItemInfo = itemInfoGather.copy()
            result.append(copyItemInfo)
            itemInfoGather.clear()

    driver.close()
    return result