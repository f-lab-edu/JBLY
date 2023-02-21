from bs4 import BeautifulSoup
import requests

def getTitle():
    url = "https://programmers.co.kr"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    print(soup.title)
    return None
