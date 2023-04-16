from collections import defaultdict
from urlCollection import url_collection_module
from crawlingSite import CrawlingPageModule
from util import chunker
from detailPage import DetailPageUrlProcess, DetailPageCrawlingModule
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
    items_lists = CrawlingPageModule.crawling_page(page_items)
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
    detail_pages = DetailPageUrlProcess.get_detail_info_response(chunked_detail_requests)

    # 상세 페이지 CPU Bound 작업
    crawling_detail_pages = DetailPageCrawlingModule.crawling_site(detail_pages)

    # 기존에 존재하는 아이템 리스트의 아이템 이름과 상세 페이지 리스트의 아이템 이름을 비교해 같다면 상세 페이지 html 소스를 리스트에 추가
    for crawling_detail_page in crawling_detail_pages:
        item_name, detail_html_source = crawling_detail_page
        for crawling_total_item in crawling_total_items:
            if crawling_total_item[1] == item_name:
                crawling_total_item.extend(detail_html_source)

    logging.info(f"크롤링한 아이템 수는 : {len(crawling_total_items)} 입니다.")

    # crawling_total_items를 DB에 insert해야 합니다.