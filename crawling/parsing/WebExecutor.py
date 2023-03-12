from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def executor():

  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('headless')
  chrome_options.add_argument('window-size=1920x1080')
  chrome_options.add_argument("disable-gpu")
  return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

