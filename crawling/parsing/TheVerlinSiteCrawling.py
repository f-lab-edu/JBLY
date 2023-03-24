from selenium.webdriver.common.by import By
from parsing.ProductTypes import product_types
from bs4 import BeautifulSoup
import requests
import re
import time
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


def get_total_item_list(driver):

    shop_id = 3
    store_name = "theverlin"

    result = []
    urls = []
    urls.append(("https://theverlin.com/product/list.html?cate_no=42", product_types.OUTWEAR.name))  # outwear
    urls.append(("https://theverlin.com/product/list.html?cate_no=43", product_types.TOP.name))  # top
    urls.append(("https://theverlin.com/product/list.html?cate_no=44", product_types.BOTTOM.name))  # bottom
    urls.append(("https://theverlin.com/product/list.html?cate_no=48", product_types.ACCESSORY.name))  # acc
    urls.append(("https://theverlin.com/category/shoes/193/", product_types.SHOES.name))  # shoes
    base_url = "https://theverlin.com/"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

    for url in urls:
        each_url, item_type = url
        driver.get(eachUrl)

        while True:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            datas = soup.find("ul", "prdList column4").find_all("li", recursive=False)
            datas = list(map(str, datas))

            for data in datas:
                item_info_gather = []
                each_data = BeautifulSoup(data, 'html.parser')
                get_image_url = each_data.find('img')['src']
                image_url = 'https:' + get_image_url

                # get Item
                get_item_name = each_data.find('p', {'class': 'name'})
                item_name = get_item_name.text.replace('\n', '')
                item_name = item_name.split(': ')[1]

                # get Price
                try:
                    item = each_data.find("ul", "xans-element- xans-product xans-product-listitem").find_all("span")
                    item = list(map(str, item))

                    temp = ""
                    for i in item:
                        if '￦' in i:
                            temp = i
                            break
                except:
                    pass

                soup = BeautifulSoup(temp, "html.parser")
                get_price = soup.text
                price = re.sub(r'\D', '', get_price)

                # get detail info
                detail = each_data.find('a')['href']
                detail_info = base_url + detail

                # get detail information html
                header = {
                    'Referrer': detail_info,
                    'user-agent': user_agent
                }
                response = requests.get(detail_info, headers=header)
                b_soup = BeautifulSoup(response.text, 'html.parser')
                detail_html = b_soup.find("div", "cont")

                item_info_gather.append(store_name)
                item_info_gather.append(item_name)
                item_info_gather.append(image_url)
                item_info_gather.append(price)
                item_info_gather.append(item_type)
                item_info_gather.append(detail_info)
                item_info_gather.append(shop_id)
                item_info_gather.append(detail_html)
                copy_item_info = item_info_gather.copy()
                result.append(copy_item_info)
                item_info_gather.clear()

            # page 이동
            element = driver.find_element(by=By.XPATH, value='//*[@id="contents"]/div/div[4]/p[3]/a')
            driver.implicitly_wait(10)

            if element.is_displayed() and element.is_enabled():
                try:
                    driver.execute_script("arguments[0].click();", element)
                except:
                    pass
            if driver.current_url.endswith("#none"):
                break
    return result
