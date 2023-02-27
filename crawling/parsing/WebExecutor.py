from selenium import webdriver

def executor():
  return webdriver.Chrome(executable_path='C:\chromedriver.exe')