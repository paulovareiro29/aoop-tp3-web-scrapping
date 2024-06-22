import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_document_height(driver):
  return driver.execute_script("return document.body.scrollHeight")
  
def scroll_document_to_bottom(driver):
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

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

def search_by_keywords(driver, keywords):
  query = ""
  for keyword in keywords:
    query += "%23" + keyword.replace(" ", "%20")
    
  driver.get("https://x.com/search?q=" + query)
  
def sanitize_tweet(tweet):
  # Remove URLs
  tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
  # Remove special characters and punctuation
  tweet = re.sub(r'[^A-Za-z0-9\s]+', '', tweet)
  # Replace line breaks with a space
  tweet = tweet.replace('\n', ' ').replace('\r', ' ')
  # Replace multiple spaces with a single space
  tweet = re.sub(r'\s{2,}', ' ', tweet)
  # Convert to lowercase
  tweet = tweet.lower()
  # Remove extra whitespace
  tweet = tweet.strip() 
  return tweet

def is_valid_tweet(tweet):
  # Length check: Ensure the text has a minimum length
  if len(tweet) < 10:
      return False
  # Alpha check: Ensure the text contains alphabetic characters
  if not any(char.isalpha() for char in tweet):
      return False
  # Additional checks can be added as needed
  return True

def scrap_tweets(driver, limit = 100):
  scrapped_tweets = set()

  last_height = get_document_height(driver)

  while True:
    scroll_document_to_bottom(driver)
    time.sleep(10)
    
    current_height = get_document_height(driver)
    
    if current_height == last_height or len(scrapped_tweets) >= limit:
      break
    
    last_height = current_height
    
    tweets = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
    
    for tweet in tweets:
      try:
        tweet_text = sanitize_tweet(tweet.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text)
        
        if is_valid_tweet(tweet_text) and tweet_text not in scrapped_tweets:
            scrapped_tweets.add(tweet_text)

      except Exception as e:
        print(e)
        continue

  return scrapped_tweets