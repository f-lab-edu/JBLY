from bs4 import BeautifulSoup

def get_detail_page(response, item_name):
    get_detail_html = BeautifulSoup(response.text, 'html.parser')
    detail_html = get_detail_html.find('div', {'id': 'prdDetail'})
    return [item_name, detail_html]