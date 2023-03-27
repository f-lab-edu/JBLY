from collections import defaultdict


def url_chunk(urls):
    chunked_urls = defaultdict(list)
    chunk_size = 7

    for url in urls:
        for shop_name in url.keys():
            total_elements = url[shop_name]
            chunk_data = [total_elements[i:i + chunk_size] for i in range(0, len(total_elements), chunk_size)]
            chunked_urls[shop_name].extend(chunk_data)
    return chunked_urls

def detail_info_chink():
    return None
