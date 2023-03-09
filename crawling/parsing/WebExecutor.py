from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def executor():


  chromeOptions = Options()
  chromeOptions.add_argument('--no-sandbox')
  chromeOptions.add_argument('--disable-dev-shm-usage')
  chromeOptions.binary_location = "./chromedriver"
  return webdriver.Chrome(executable_path=chromeOptions)

