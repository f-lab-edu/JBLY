from bs4 import BeautifulSoup
import urllib.request

def get(max_count = 1):
    base_url = "http"
    url = ""

    count = 1
    while count <= max_count:
        html = urllib.request.urlopen(url)
        source = html.read()

        soup= BeautifulSoup(source, "html.parser")

        img = soup.find("img") # 이미지 태그
        img_src = img.get("src") # 이미지 경로
        img_url = base_url + img_src #



<img src="//theverlin.com/web/product/medium/202205/735204348beea31c35def11f081c0035.png" id="eListPrdImage4021_1" alt="" class="thumb">

< img
src = "//theverlin.com/web/product/medium/202204/36cce684d0efa713f1867f5d9fc085de.gif"
id = "eListPrdImage4016_1"
alt = ""


class ="thumb" >