from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_detail_page(response, item_name):
    get_detail_html = BeautifulSoup(response.text, 'html.parser')
    detail_html = get_detail_html.find("div", "cont")
    return [item_name, detail_html]