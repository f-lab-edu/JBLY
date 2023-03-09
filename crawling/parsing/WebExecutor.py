from selenium import webdriver

def executor():

  # chrome_options = webdriver.ChromeOptions()
  # chrome_options.add_argument('--headless')
  # chrome_options.add_argument('--no-sandbox')
  # chrome_options.add_argument('--disable-dev-shm-usage')
  # chromedriver = "./chromedriver"
  # executable_path=chromedriver, options=chrome_options
  return webdriver.Chrome()

