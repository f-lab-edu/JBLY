import multiprocessing
import importlib

sub_directory_name = "detailPage"

def run_job(crawling_site):
    shop_name, item_name, response = crawling_site
    module_name = sub_directory_name + "." + shop_name + "DetailPageCrawling"
    module = importlib.import_module(module_name)
    return module.get_detail_page(response, item_name)

def crawling_site(detail_sites): # input : ['morecherry', '플랫폼 라운드 로퍼 앵클 .47 (2color)', <Response [200]>]
    output = []
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        results = pool.imap(run_job, detail_sites)
        for result in results:
            output.append(result)
    return output