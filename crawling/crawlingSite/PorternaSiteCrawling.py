from bs4 import BeautifulSoup
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://porterna.com"
shop_id = 1
store_name = "porterna"

def get_total_products(response, item_type):
    result = [] # storeName, itemName, getUrl, get_price, itemType, shopId

    soup = BeautifulSoup(response.text, 'html.parser')

    datas = soup.find("ul", "thumbnail").find_all("li", recursive=False)

    for data in datas:
        item_info_gather = []

        # get Image
        get_image_url = data.find('img')['src']
        image_url = 'https:' + get_image_url

        # get detail info
        get_detail_info = data.find('a')['href']
        detail_info = base_url + get_detail_info

        # get ItemName
        get_item_name = data.find('p', {'class': 'name'})
        item_name = get_item_name.text

        # get Price
        get_price = data.find('div', {'class': 'price1'})
        price = get_price.text
        price = re.sub(r'\D', '', price)

        item_info_gather.append(store_name)
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