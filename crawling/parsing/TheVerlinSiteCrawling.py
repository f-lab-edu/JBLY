from parsing.ProductTypes import productTypes
from bs4 import BeautifulSoup
import requests
import ssl
import re


ssl._create_default_https_context = ssl._create_unverified_context


def getTotalProducts():

    shopId = 3
    storeName = "theverlin"

    result = []
    urls = []
    urls.append(("https://theverlin.com/product/list.html?cate_no=42&page=", productTypes.OUTWEAR.name))  # outwear
    urls.append(("https://theverlin.com/product/list.html?cate_no=43&page=", productTypes.TOP.name))  # top
    urls.append(("https://theverlin.com/product/list.html?cate_no=44&page=", productTypes.BOTTOM.name))  # bottom
    urls.append(("https://theverlin.com/product/list.html?cate_no=48&page=", productTypes.ACCESSORY.name))  # acc
    urls.append(("https://theverlin.com/category/shoes/193/?page=", productTypes.SHOES.name))  # shoes
    baseUrl = "https://theverlin.com/"
    userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

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
                datas = soup.find("ul", "prdList column4").find_all("li", recursive=False)
            except:
                break

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
                getDetailHtmlResponse = requests.get(detailInfo, headers= header)
                getDetailHtml = BeautifulSoup(getDetailHtmlResponse.text, 'html.parser')
                detailHtml = getDetailHtml.find("div", "cont")

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