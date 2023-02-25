import re

from bs4 import BeautifulSoup
from urllib.request import urlopen

#
# url='https://theverlin.com/product/list.html?cate_no=43&page='
# f = open("theverlin_top.json", 'w', encoding='UTF8')
# for i in range(1,6):
#     fullurl = url+str(i)
#     html = urlopen(fullurl)
#     soup = BeautifulSoup(html, 'html.parser')
#     for anchor in soup.find_all('ul', class_='xans-element- xans-product xans-product-listitem'):
#         data = anchor.get_text()
#         f.write(data)
#         for line in data.splitlines():
#
#             matches = re.findall(r"￦\s+\d+", line)
#             if matches:
#                 f.write("".join(matches) + "\n")
# f.close()

url='https://theverlin.com/product/list.html?cate_no=43&page='
f = open("theverlin_top.json", 'w', encoding='UTF8')
for i in range(1,6):
    fullurl = url+str(i)
    html = urlopen(fullurl)
    soup = BeautifulSoup(html, 'html.parser')

    while cound <





