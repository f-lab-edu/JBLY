import os
import requests
from concurrent.futures import ThreadPoolExecutor


def detail_url_scraper(target_url):
    href_list = []
    for page_num in range(1, find_last_page(target_url) + 1):
        header = {
            'Referrer': target_url + str(page_num),
            'user-agent': user_agent
        }
        response = requests.get(target_url + str(page_num), headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.find_all('ul', {'class': 'prdList grid4'})
        href_set = set()
        for ul_tag in soup:
            a_tags = ul_tag.find_all('a')
            for a_tag in a_tags:
                href = a_tag.get('href')
                if href is not None:
                    href_set.add(href)
        href_list += list(href_set)
    return None


if __name__ == '__main__':
    urls = [
        ("https://more-cherry.com/category/outwear/24/?page=", productTypes.OUTWEAR.name),
        ("https://more-cherry.com/category/top/25/?page=", productTypes.TOP.name),
        ("https://more-cherry.com/category/pants/26/?page=", productTypes.BOTTOM.name),
        ("https://more-cherry.com/category/accessory/28/?page=", productTypes.ACCESSORY.name),
        ("https://more-cherry.com/category/shoes/42/?page=", productTypes.SHOES.name),
    ]

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(detail_url_scraper, urls)


