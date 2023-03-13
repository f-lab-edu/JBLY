from selenium.webdriver.common.by import By
from parsing.ProductTypes import productTypes
from parsing import WebExecutor
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
import ssl
import re


ssl._create_default_https_context = ssl._create_unverified_context

def getTotalProducts():
    # WebDriver를 초기화합니다.
    driver = WebExecutor.executor()

    # Var Setting
    shopId = 2
    storeName = "morecherry"
    result = [] # storeName, itemName, imageUrl, price, itemType, shopId
    urls = []
    urls.append(("https://more-cherry.com/category/outwear/24",productTypes.OUTWEAR.name))  # outwear
    urls.append(("https://more-cherry.com/category/top/25", productTypes.TOP.name))  # top
    urls.append(("https://more-cherry.com/category/pants/26",productTypes.BOTTOM.name))  # bottom
    urls.append(("https://more-cherry.com/category/accessory/28",productTypes.ACCESSORY.name))  # acc
    urls.append(("https://more-cherry.com/category/shoes/42",productTypes.SHOES.name))  # shoes
    baseUrl = "https://more-cherry.com"
    userAgent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36"

    for url in urls:
        eachUrl, itemType = url
        driver.get(eachUrl)
        while True:

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            datas = soup.find("ul", "prdList grid4").find_all("li", recursive=False)
            datas = list(map(str, datas))

            for data in datas:

                itemInfoGather = []
                eachData = BeautifulSoup(data, 'html.parser')

                #get Image
                getImageUrl = eachData.find('img')['src']
                imageUrl = 'https:' + getImageUrl

                # get detail Info
                getDetailInfo = eachData.find('a')['href']
                detailInfo = baseUrl + getDetailInfo

                # get ItemName
                getItemName = eachData.find('span', {'class': 'name'})
                getItemName = getItemName.text
                itemName = getItemName.split(' : ')[-1]

                # get Price
                getPrice = eachData.find('ul', {'class': 'xans-element- xans-product xans-product-listitem spec'})
                price = getPrice.text
                price = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', price)[0].replace(",", "")

                # get detail info HTML
                temp = list(getDetailInfo.split("/"))
                encodeBytes = quote(temp[2])
                temp[2] = encodeBytes
                encodedDetailInfo = "/".join(temp)
                detailInfo = baseUrl + encodedDetailInfo

                # setting referrer and userAgent
                header = {
                    'Referrer': detailInfo,
                    'user-agent': userAgent
                }

                response = requests.get(detailInfo, headers=header)
                bSoup = BeautifulSoup(response.text, 'html.parser')
                detailHtml = bSoup.find('div', {'id': 'prdDetail'})

                itemInfoGather.append(storeName)
                itemInfoGather.append(itemName)
                itemInfoGather.append(imageUrl)
                itemInfoGather.append(price)
                itemInfoGather.append(itemType)
                itemInfoGather.append(detailInfo)
                itemInfoGather.append(shopId)
                itemInfoGather.append(detailHtml)
                copyItemInfo = itemInfoGather.copy()
                result.append(copyItemInfo)
                itemInfoGather.clear()

            element = driver.find_element(by=By.XPATH, value='//*[@id="contents2"]/div[3]/a[3]')
            driver.implicitly_wait(10)

            if element.is_displayed() and element.is_enabled():
                try:
                    driver.execute_script("arguments[0].click();", element)
                except:
                    pass
            if driver.current_url.endswith("#none"):
                break

    driver.close()
    return result