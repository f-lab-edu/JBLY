from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def executor():


  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  chromeDriverPath = "./chromedriver"
  return webdriver.Chrome(executable_path=chromeDriverPath)

