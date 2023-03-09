from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def executor():

  chromeDriverPath = "./chromedriver"
  return webdriver.Chrome(executable_path=chromeDriverPath)

