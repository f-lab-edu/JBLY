from parsing.ProductTypes import productTypes
from bs4 import BeautifulSoup
import requests
import ssl
import re


ssl._create_default_https_context = ssl._create_unverified_context


def getTotalProducts():

    shopId = 1
    storeName = "porterna"
    result = [] # storeName, itemName, getUrl, getPrice, itemType, shopId
    urls = []
    urls.append(("https://porterna.com/product/list.html?cate_no=541&page=", productTypes.OUTWEAR.name)) # outwear
    urls.append(("https://porterna.com/product/list.html?cate_no=789&page=", productTypes.TOP.name)) # top
    urls.append(("https://porterna.com/product/list.html?cate_no=28&page=", productTypes.BOTTOM.name)) # bottom
    urls.append(("https://porterna.com/product/list.html?cate_no=44&page=", productTypes.ACCESSORY.name)) # acc
    urls.append(("https://porterna.com/product/list.html?cate_no=79&page=", productTypes.SHOES.name)) # shoes
    baseUrl = "https://porterna.com"

    for url in urls:
        eachUrl, itemType = url
        urlSequence = 1
        header = {
            'Referrer': baseUrl,
            'user-agent': userAgent
        }
        while True:
            currentPageUrl = eachUrl + str(urlSequence)
            urlSequence += 1
            response = requests.get(currentPageUrl, headers=header)
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                datas = soup.find("ul", "thumbnail").find_all("li", recursive=False)
            except:
                break

            for data in datas:
                itemInfoGather = []

                # get Image
                getImageUrl = data.find('img')['src']
                imageUrl = 'https:' + getImageUrl

                # get detail info
                getDetailInfo = data.find('a')['href']
                detailInfo = baseUrl + getDetailInfo

                # get ItemName
                getItemName = data.find('p', {'class': 'name'})
                itemName = getItemName.text

                # get Price
                getPrice = data.find('div', {'class': 'price1'})
                price = getPrice.text
                price = re.sub(r'\D', '', price)

                getDetailHtmlResponse = requests.get(detailInfo, headers= header)
                getDetailHtml = BeautifulSoup(getDetailHtmlResponse.text, 'html.parser')
                detailHtml = getDetailHtml.find("div", {'class': 'pr-header'})

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

    return result