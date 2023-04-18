from collections import defaultdict
from urlCollection import url_collection_module
from crawlingSite import crawling_page_module
from util import chunker
from detailPage import detail_page_url_process, detail_page_crawling_module
from dbConnection import database_module
import logging

logging.basicConfig(level=logging.INFO)

def run():

    # 크롤링 대상 페이지 모음
    total_pages = url_collection_module.url_collecting()

    shop_name_and_headers = defaultdict(list) # { shop_name : [base_url, user_agent]} 갖고 있어 상세 페이지 접근을 위해 사용
    page_items = [] # 페이지를 리스트로 갖고 있는 변수

    for page in total_pages:
        site_total_responses, base_url, user_agent, shop_name = page
        page_items.extend(site_total_responses)
        shop_name_and_headers[shop_name].append((base_url, user_agent))

    # 모은 대상 페이지 Crawling
    items_lists = crawling_page_module.crawling_page(page_items)
    crawling_total_items = [] # 크롤링한 아이템 리스트
    for items_list in items_lists:
        crawling_total_items.extend(items_list)

    # 아이템 리스트에서 상세 페이지 주소 추출 뒤 I/O 작업 진행
    extract_detail_page_url = list(map(lambda x: x[:1] + x[1:2] + x[5:6], crawling_total_items))  # [shop_name, item_name, detail_info_url]
    detail_page_request_list = [] # 상세 페이지에 접근하기 위해 필요한 header 값들을 담고 있는 리스트 [shop_name, detail_info_url, item_name, headers ]

    for extract_page in extract_detail_page_url:
        shop_name, item_name, detail_info_url = extract_page
        temp_detail_list = [shop_name, item_name, detail_info_url]
        if shop_name in shop_name_and_headers:
            header_values = shop_name_and_headers[shop_name]
            temp_detail_list.extend(header_values)
            detail_page_request_list.append(temp_detail_list)

    # 상세 페이지 request 작업
    chunked_detail_requests = chunker.detail_urls_chunker(detail_page_request_list)
    detail_pages = detail_page_url_process.get_detail_info_response(chunked_detail_requests)  # [shop_name, item_name, response]

    # 상세 페이지 CPU Bound 작업
    crawling_detail_pages = detail_page_crawling_module.crawling_site(detail_pages) # [item_name, detail_html]

    # 기존에 존재하는 아이템 리스트의 아이템 이름과 상세 페이지 리스트의 아이템 이름을 비교해 같다면 상세 페이지 html 소스를 리스트에 추가
    for crawling_detail_page in crawling_detail_pages:
        item_name, detail_html_source = crawling_detail_page
        for crawling_total_item in crawling_total_items:
            if crawling_total_item[1] == item_name:
                crawling_total_item.append(detail_html_source)

    logging.info(f"크롤링된 전체 상품 수는 : {len(crawling_total_items)} 입니다.")

    '''
    Product Type이 중복된 상품은 detail_page가 하나 더 추가되어 데이터 형식에 맞지 않게 됩니다.
    일단, 강제로 데이터의 길이를 8로 맞추고 프로젝트를 진행합니다.
    '''
    insert_data_capa = 8
    for index in range(len(crawling_total_items)):
        if len(crawling_total_items[index]) != insert_data_capa:
            crawling_total_items[index] = crawling_total_items[index][:insert_data_capa]

    crawling_datas = crawling_data_list_to_dict(crawling_total_items)
    database_module.run(crawling_datas)

'''
[{'shopName' : shopName, 
 'productName' : productName, 
 'image' : image, 
 'price' : price, 
 'productType' : productType, 
 'detailInfo' : detailInfo, 
 'shopId' : shopId, 
 'detailHtml' : detailHtml} .. 
]
'''
def crawling_data_list_to_dict(crawling_data):
    return [{
        'shopName': shopName,
        'productName': productName,
        'image': image,
        'price': price,
        'productType': productType,
        'detailInfo': detailInfo,
        'shopId': shopId,
        'detailHtml': detailHtml
    } for shopName, productName, image, price, productType, detailInfo, shopId, detailHtml in crawling_data]
