from bs4 import BeautifulSoup
import requests
import ssl
import re


ssl._create_default_https_context = ssl._create_unverified_context

baseUrl = "https://porterna.com"
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
shopId = 1
storeName = "porterna"
header = {
    'Referrer': baseUrl,
    'user-agent': userAgent
}

def getTotalProducts(responses):
    result = [] # storeName, itemName, getUrl, getPrice, itemType, shopId

    for each_response in responses:
        response, item_type = each_response
        soup = BeautifulSoup(response.text, 'html.parser')

        datas = soup.find("ul", "thumbnail").find_all("li", recursive=False)

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
            itemInfoGather.append(item_type)
            itemInfoGather.append(detailInfo)
            itemInfoGather.append(shopId)
            itemInfoGather.append(detailHtml)
            copyItemInfo = itemInfoGather.copy()
            result.append(copyItemInfo)
            itemInfoGather.clear()

    print(storeName, " current length of product is = ", len(result))
    return result