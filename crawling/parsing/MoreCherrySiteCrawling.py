from bs4 import BeautifulSoup
import requests
import ssl
import re


ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://more-cherry.com"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36"
shop_id = 2
store_name = "morecherry"
header = {
            'Referrer': base_url,
            'user-agent': user_agent
}

# 각 Process 당 7개의 페이지를 크롤링하는 책임을 갖고 있습니다.
def get_total_products(responses):
    result = []  # storeName, itemName, imageUrl, price, itemType, shopId

    for each_response in responses:
        response, item_type = each_response
        soup = BeautifulSoup(response.text, 'html.parser')

        datas = soup.find("ul", "prdList grid4").find_all("li", recursive=False) # return NoneType

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
            detailInfo = base_url + getDetailInfo

            # getDetailHtmlResponse = requests.get(detailInfo, headers=header)
            # getDetailHtml = BeautifulSoup(getDetailHtmlResponse.text, 'html.parser')
            # detailHtml = getDetailHtml.find('div', {'id': 'prdDetail'})

            itemInfoGather.append(store_name)
            itemInfoGather.append(itemName)
            itemInfoGather.append(imageUrl)
            itemInfoGather.append(price)
            itemInfoGather.append(item_type)
            itemInfoGather.append(detailInfo)
            itemInfoGather.append(shop_id)
            # itemInfoGather.append(detailHtml)
            copyItemInfo = itemInfoGather.copy()
            result.append(copyItemInfo)
            itemInfoGather.clear()

    return result
