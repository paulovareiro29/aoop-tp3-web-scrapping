# pip install selenium
# pip install python-dotenv

import os
import time
from dotenv import load_dotenv
from lib import create_web_driver, login_to_twitter, search_by_keywords, scrap_tweets
from selenium.webdriver.support.ui import WebDriverWait

import csv

load_dotenv()

username = os.getenv("TWITTER_USERNAME")
password = os.getenv("TWITTER_PASSWORD")

driver = create_web_driver()
wait = WebDriverWait(driver, 20)

login_to_twitter(driver, username, password)

time.sleep(5)

cryptocurrencies = ["bitcoin", "ethereum"]
sentiments = ["bullish", "bearish"]

collected_tweets = set()

with open('./data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Cryptocurrency", "Sentiment", "Tweet"])
    file.close()

for cryptocurrency in cryptocurrencies:
    for sentiment in sentiments:
        search_by_keywords(driver, [cryptocurrency, sentiment])
        time.sleep(10)
        
        tweets = scrap_tweets(driver, 10)
        
        with open('./data.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for tweet in tweets:
                writer.writerow([cryptocurrency, sentiment, tweet])

time.sleep(10)

driver.quit()