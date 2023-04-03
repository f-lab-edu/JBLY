from bs4 import BeautifulSoup
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://more-cherry.com"
shop_id = 2
shop_name = "morecherry"


def get_total_products(response, item_type):
    result = []  # storeName, itemName, imageUrl, price, itemType, shopId

    soup = BeautifulSoup(response.text, 'html.parser')

    datas = soup.find("ul", "prdList grid4").find_all("li", recursive=False)  # return NoneType

    for data in datas:
        item_info_gather = []
        # get Image
        get_image_url = data.find('img')['src']
        image_url = 'https:' + get_image_url

        # get ItemName
        get_item_name = data.find('span', {'class': 'name'})
        get_item_name = get_item_name.text
        item_name = get_item_name.split(' : ')[-1]

        # get Price
        get_price = data.find('ul', {'class': 'xans-element- xans-product xans-product-listitem spec'})
        price = get_price.text
        price = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', price)[0].replace(",", "")

        # get detail Info
        get_detail_info = data.find('a')['href']
        detail_info = base_url + get_detail_info

        item_info_gather.append(shop_name)
        item_info_gather.append(item_name)
        item_info_gather.append(image_url)
        item_info_gather.append(price)
        item_info_gather.append(item_type)
        item_info_gather.append(detail_info)
        item_info_gather.append(shop_id)
        copy_item_info = item_info_gather.copy()
        result.append(copy_item_info)
        item_info_gather.clear()

    return result
