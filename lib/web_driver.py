from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_web_driver():
  chrome_options = Options()
  # chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-gpu")

  service = Service(executable_path="./lib/chromedriver.exe")
  return webdriver.Chrome(service=service, options = chrome_options)