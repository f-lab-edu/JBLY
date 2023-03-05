# from selenium import webdriver
# import platform
#
# def executor():
#
#   osType = platform.system()
#
#   if osType == "Linux" or osType == "Darwin":
#     return webdriver.Chrome()
#
#   return webdriver.Chrome(executable_path='C:\chromedriver.exe')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def executor():
  chrome_options = webdriver.ChromeOptions()
  return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
