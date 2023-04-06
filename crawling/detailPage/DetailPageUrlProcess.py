from detailPage import DetailPageUrlThread
import multiprocessing

def get_detail_info_response(chunked_detail_urls):
    output = []
    with multiprocessing.Pool(3) as pool:
        results = pool.imap(DetailPageUrlThread.get_total_detail_info_response, chunked_detail_urls)
        for result in results:
            output.extend(result)
    return output