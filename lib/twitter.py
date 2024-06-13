from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_twitter(driver, username, password):
  """
  Logs into Twitter using the provided WebDriver, username, and password.
  
  :param driver: WebDriver instance.
  :param username: Twitter username.
  :param password: Twitter password.
  """
  driver.get("https://x.com/login")
  wait = WebDriverWait(driver, 10)

  username_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
  username_input.send_keys(username)

  next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@role="button"]//span[text()="Avançar"]')))
  next_btn.click()

  password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
  password_input.send_keys(password)

  submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@role="button"]//span[text()="Entrar"]')))
  submit_btn.click()
