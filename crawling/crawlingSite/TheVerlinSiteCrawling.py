from bs4 import BeautifulSoup
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://theverlin.com/"
shop_id = 3
shop_name = "theverlin"

def get_total_products(response, item_type):
    result = []

    soup = BeautifulSoup(response.text, 'html.parser')

    datas = soup.find("ul", "prdList column4").find_all("li", recursive=False)

    for data in datas:
        item_info_gather = []
        # get Image
        get_image_url = data.find('img')['src']
        image_url = 'https:' + get_image_url

        # get Item
        get_item_name = data.find('p', {'class': 'name'})
        item_name = get_item_name.text.replace('\n', '')
        item_name = item_name.split(': ')[1]

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

        # theverlin의 경우 이름표 상품에 가격이 존재하지 않아 예외가 발생합니다.
        try:
            temp = list(temp.split("￦ "))
            temp = temp[1].split("<")[0]
            temp = temp.replace(',', '')
        except:
            continue

        price = temp

        # get detail info
        detail = data.find('a')['href']
        detail_info = base_url + detail


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