from selenium import webdriver
import platform

def executor():

  osType = platform.system()

  if osType == "Linux" or osType == "Darwin":
    return webdriver.Chrome()

  return webdriver.Chrome(executable_path='C:\chromedriver.exe')