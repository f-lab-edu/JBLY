from parsing.ProductTypes import productTypes
from bs4 import BeautifulSoup
import requests
import ssl
import re


ssl._create_default_https_context = ssl._create_unverified_context

def getTotalProducts():

    # Var Setting
    shopId = 2
    storeName = "morecherry"
    result = [] # storeName, itemName, imageUrl, price, itemType, shopId
    urls = []
    urls.append(("https://more-cherry.com/category/outwear/24/?page=",productTypes.OUTWEAR.name))  # outwear
    urls.append(("https://more-cherry.com/category/top/25/?page=", productTypes.TOP.name))  # top
    urls.append(("https://more-cherry.com/category/pants/26/?page=",productTypes.BOTTOM.name))  # bottom
    urls.append(("https://more-cherry.com/category/accessory/28/?page=",productTypes.ACCESSORY.name))  # acc
    urls.append(("https://more-cherry.com/category/shoes/42/?page=",productTypes.SHOES.name))  # shoes
    baseUrl = "https://more-cherry.com"
    userAgent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36"

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
            response = requests.get(currentPageUrl, headers= header)
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                datas = soup.find("ul", "prdList grid4").find_all("li", recursive=False) # return NoneType
            except:
                break

            for data in datas:
                itemInfoGather = []
                # get Image
                getImageUrl = data.find('img')['src']
                imageUrl = 'https:' + getImageUrl

                # get ItemName
                getItemName = data.find('span', {'class': 'name'})
                getItemName = getItemName.text
                itemName = getItemName.split(' : ')[-1]

                # get Price
                getPrice = data.find('ul', {'class': 'xans-element- xans-product xans-product-listitem spec'})
                price = getPrice.text
                price = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', price)[0].replace(",", "")

                # get detail Info
                getDetailInfo = data.find('a')['href']
                detailInfo = baseUrl + getDetailInfo

                getDetailHtmlResponse = requests.get(detailInfo, headers=header)
                getDetailHtml = BeautifulSoup(getDetailHtmlResponse.text, 'html.parser')
                detailHtml = getDetailHtml.find('div', {'id': 'prdDetail'})

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
