from selenium.webdriver.common.by import By
from parsing.ProductTypes import productTypes
from bs4 import BeautifulSoup
import requests
import ssl
import re


ssl._create_default_https_context = ssl._create_unverified_context


def getTotalProducts(driver):

    shopId = 1
    storeName = "porterna"
    result = [] # storeName, itemName, getUrl, getPrice, itemType, shopId
    urls = []
    urls.append(("https://porterna.com/product/list.html?cate_no=541", productTypes.OUTWEAR.name)) # outwear
    urls.append(("https://porterna.com/product/list.html?cate_no=789", productTypes.TOP.name)) # top
    urls.append(("https://porterna.com/product/list.html?cate_no=28", productTypes.BOTTOM.name)) # bottom
    urls.append(("https://porterna.com/product/list.html?cate_no=44", productTypes.ACCESSORY.name)) # acc
    urls.append(("https://porterna.com/product/list.html?cate_no=79", productTypes.SHOES.name)) # shoes
    baseUrl = "https://porterna.com"
    userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

    for url in urls: # itemType에 따른 url init
        eachUrl, itemType = url
        driver.get(eachUrl)
        while True:

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            datas = soup.find("ul", "thumbnail").find_all("li", recursive=False)
            datas = list(map(str, datas))

            for data in datas:
                itemInfoGather = []
                eachData = BeautifulSoup(data, 'html.parser')

                # get Image
                getImageUrl = eachData.find('img')['src']
                imageUrl = 'https:' + getImageUrl

                # get detail info
                getDetailInfo = eachData.find('a')['href']
                detailInfo = baseUrl + getDetailInfo

                # get ItemName
                getItemName = eachData.find('p', {'class': 'name'})
                itemName = getItemName.text

                # get Price
                getPrice = eachData.find('div', {'class': 'price1'})
                price = getPrice.text
                price = re.sub(r'\D', '', price)

                # get detail information html
                header = {
                    'Referrer': detailInfo,
                    'user-agent': userAgent
                }

                response = requests.get(detailInfo, headers= header)
                bSoup = BeautifulSoup(response.text, 'html.parser')
                detailHtml = bSoup.find("div", {'class': 'pr-header'})

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

            # page 이동
            element = driver.find_element(by=By.XPATH, value='//*[@id="contents"]/div[2]/div[4]/a[2]')
            driver.implicitly_wait(10)

            if element.is_displayed() and element.is_enabled():
                try:
                    driver.execute_script("arguments[0].click();", element)
                except:
                    pass
            if driver.current_url.endswith("#none"):
                break

    return result