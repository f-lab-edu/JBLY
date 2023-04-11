import requests
import concurrent.futures

def fetch_url(each_url):
    shop_name, item_name, detail_info_url, header_values = each_url
    base_url, user_agent = header_values
    header = {
        'Referrer': base_url,
        'user-agent': user_agent
    }
    response = requests.get(detail_info_url, headers=header)
    return [shop_name, item_name, response]

'''
input : ['레이스 반 스타킹 (2color)', 'https://more-cherry.com/product/레이스-반-스타킹-2color/20163/category/28/display/1/', ('https://more-cherry.com', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36')]
output : [shop_name, item_name, detail_page_response]
'''
def get_total_detail_info_response(url):
    output = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        results = executor.map(fetch_url, url)
        for result in results:
            output.append(list(result))

    return output
