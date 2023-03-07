import re

import requests
from selenium.webdriver.common.by import By
from parsing.ProductTypes import productTypes
from parsing import WebExecutor
from bs4 import BeautifulSoup
import re
import time
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


def getTotalItemList():
    browser = WebExecutor.executor()
    detailBrowser = WebExecutor.executor()
    shopId = 3
    storeName = "theverlin"

    result = []
    urls = []
    urls.append(("https://theverlin.com/product/list.html?cate_no=42", productTypes.OUTWEAR.name))  # outwear
    urls.append(("https://theverlin.com/product/list.html?cate_no=43", productTypes.TOP.name))  # top
    urls.append(("https://theverlin.com/product/list.html?cate_no=44", productTypes.BOTTOM.name))  # bottom
    urls.append(("https://theverlin.com/product/list.html?cate_no=48", productTypes.ACCESSORY.name))  # acc
    urls.append(("https://theverlin.com/category/shoes/193/", productTypes.SHOES.name))  # shoes

    for url in urls:
        eachUrl, itemType = url
        browser.get(eachUrl)

        while True:
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            datas = soup.find("ul", "prdList column4").find_all("li", recursive=False)  # 최상위 태그만 찾게 하기위해서 False로 지정
            datas = list(map(str, datas))

            for data in datas:

                itemInfoGather = []
                eachData = BeautifulSoup(data, 'html.parser')
                getImageUrl = eachData.find('img')['src']
                imageUrl = 'https:' + getImageUrl

                # get Item
                getItemName = eachData.find('p', {'class': 'name'})
                itemName = getItemName.text.replace('\n', '')
                itemName = itemName.split(': ')[1]

                # get Price
                try:
                    item = eachData.find("ul", "xans-element- xans-product xans-product-listitem").find_all("span")
                    item = list(map(str, item))

                    temp = ""
                    for i in item:
                        if '￦' in i:
                            temp = i
                            break
                except:
                    pass

                soup = BeautifulSoup(temp, "html.parser")
                getPrice = soup.text
                price = re.sub(r'\D', '', getPrice)

                # get detail info
                detail = eachData.find('a')['href']
                detailInfo = "https://theverlin.com/" + detail

                # get detail information html

                detailBrowser.get(detailInfo)
                bSoup = BeautifulSoup(detailBrowser.page_source, 'html.parser')
                detailHtml = bSoup.find("div", "cont")

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
            element = browser.find_element(by=By.XPATH, value='//*[@id="contents"]/div/div[4]/p[3]/a')
            time.sleep(5)

            if element.is_displayed() and element.is_enabled():
                try:
                    browser.execute_script("arguments[0].click();", element)
                except:
                    pass
            if browser.current_url.endswith("#none"):
                detailBrowser.close()
                break


    browser.close()
    return result