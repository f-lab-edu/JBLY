from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def executor():

  chromeOptions = Options()
  chromeOptions.add_argument('--no-sandbox')
  chromeOptions.add_argument('--disable-dev-shm-usage')
  chromedriver = "crawling/parsing/chromedriver"
  return webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

