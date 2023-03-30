from bs4 import BeautifulSoup
import requests
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

baseUrl = "https://theverlin.com/"
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
shopId = 3
storeName = "theverlin"
header = {
    'Referrer': baseUrl,
    'user-agent': userAgent
}


def get_total_products(responses):
    result = []

    for each_response in responses:
        response, item_type = each_response
        soup = BeautifulSoup(response.text, 'html.parser')

        datas = soup.find("ul", "prdList column4").find_all("li", recursive=False)

        for data in datas:
            itemInfoGather = []
            # get Image
            getImageUrl = data.find('img')['src']
            imageUrl = 'https:' + getImageUrl

            # get Item
            getItemName = data.find('p', {'class': 'name'})
            itemName = getItemName.text.replace('\n', '')
            itemName = itemName.split(': ')[1]

            # get Price
            try:
                item = data.find("ul", "xans-element- xans-product xans-product-listitem").find_all("span")
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
            detail = data.find('a')['href']
            detailInfo = baseUrl + detail

            # get detail information html
            # getDetailHtmlResponse = requests.get(detailInfo, headers=header)
            # getDetailHtml = BeautifulSoup(getDetailHtmlResponse.text, 'html.parser')
            # detailHtml = getDetailHtml.find("div", "cont")

            itemInfoGather.append(storeName)
            itemInfoGather.append(itemName)
            itemInfoGather.append(imageUrl)
            itemInfoGather.append(price)
            itemInfoGather.append(item_type)
            itemInfoGather.append(detailInfo)
            itemInfoGather.append(shopId)
            # itemInfoGather.append(detailHtml)
            copyItemInfo = itemInfoGather.copy()
            result.append(copyItemInfo)
            itemInfoGather.clear()

    return result
