# pip install selenium
# pip install python-dotenv

import os
import time
from dotenv import load_dotenv
from lib import create_web_driver, login_to_twitter

load_dotenv()

username = os.getenv("TWITTER_USERNAME")
password = os.getenv("TWITTER_PASSWORD")

driver = create_web_driver()

login_to_twitter(driver, username, password)

time.sleep(60)

driver.quit()