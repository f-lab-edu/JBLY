import multiprocessing
import importlib

sub_directory_name = "crawlingSite"

def run_job(page_item):
    target_site, response, item_type = page_item
    target_site = sub_directory_name + "." + target_site
    module = importlib.import_module(target_site)
    return module.get_total_products(response, item_type)

'''
input : [ site_name_crawling module, <Response [200]>, 'SHOES']
output : ['morecherry', '플랫폼 라운드 로퍼 앵클 .47 (2color)', 'https://more-cherry.com/web/product/medium/202303/a3eee40ee15fe5bd0134ef995093fa46.gif', '51800', 'SHOES', 'https://more-cherry.com/product/플랫폼-라운드-로퍼-앵클-47-2color/20117/category/42/display/1/', 2]
'''
def crawling_page(page_items):
    output = []
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        results = pool.imap(run_job, page_items)
        for result in results:
            output.append(result)
    return output
