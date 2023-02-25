import re

url = "https://www.theverlin.com/product/list.html?cate_no=43"
category_number = re.search(r"cate_no=(\d+)", url).group(1)

print(category_number)