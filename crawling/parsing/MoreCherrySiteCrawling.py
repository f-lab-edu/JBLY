from selenium.webdriver.common.by import By
from parsing.ProductTypes import productTypes
from parsing import WebExecutor
from bs4 import BeautifulSoup
import time
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

def getTotalProducts():
    # WebDriver를 초기화합니다.
    driver = WebExecutor.executor()

    # Var Setting
    shopId = 2
    storeName = "morecherry"
    result = [] # storeName, itemName, imageUrl, price, itemType, shopId
    urls = []
    urls.append(("https://m.more-cherry.com/category/outwear/24",productTypes.OUTWEAR.name))  # outwear
    urls.append(("https://m.more-cherry.com/category/top/25", productTypes.TOP.name))  # top
    urls.append(("https://m.more-cherry.com/category/pants/26",productTypes.BOTTOM.name))  # bottom
    urls.append(("https://m.more-cherry.com/category/accessory/28",productTypes.ACCESSORY.name))  # acc
    urls.append(("https://m.more-cherry.com/product/list_thumb.html?cate_no=42",productTypes.SHOES.name))  # shoes

    for url in urls:
        eachUrl, itemType = url

        # 웹 페이지를 로드합니다.
        driver.get(eachUrl)
        element = driver.find_element(by=By.XPATH, value='//*[@id="contents"]/div[4]/a')

        # Get Total Page
        currentPage = driver.find_element(by=By.XPATH, value='//*[@id="more_current_page"]')
        totalPage = driver.find_element(by=By.XPATH, value='//*[@id="more_total_page"]')

        loopingTime = int(totalPage.text) - int(currentPage.text)

        for i in range(loopingTime):
            driver.execute_script("arguments[0].click();", element)
            time.sleep(5)

        detailBrowser = WebExecutor.executor()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        datas = soup.find("ul", "prdList grid2").find_all("li", recursive=False)
        datas = list(map(str, datas))  # 문자열로 변경 후
        datas = datas[1:]

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
            getPrice = getPrice.replace('원\n','')

            # get Detail Page
            getDetailInfo = targetData.find('a')['href']
            detailInfo = "https://m.more-cherry.com" + getDetailInfo

            #get detail information html
            detailBrowser.get(detailInfo)
            bSoup = BeautifulSoup(detailBrowser.page_source, 'html.parser')
            detailHtml = bSoup.find(id="prdDetail")

            # (shopName, productName, image, price, itemType, shopId, detailInfo)
            itemInfoGather.append(storeName)
            itemInfoGather.append(itemName)
            itemInfoGather.append(getUrl)
            itemInfoGather.append(getPrice)
            itemInfoGather.append(itemType)
            itemInfoGather.append(detailInfo)
            itemInfoGather.append(shopId)
            itemInfoGather.append(detailHtml)
            copyItemInfo = itemInfoGather.copy()
            result.append(copyItemInfo)
            itemInfoGather.clear()

    detailBrowser.close()
    driver.close()
    return result