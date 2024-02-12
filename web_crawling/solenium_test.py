import selenium
from selenium import webdriver


from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import time

# Set up Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the desired website
url = "https://lyricstranslate.com/en/translations/31/32/none/none/none/0/0/0/0"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Extract the HTML source code
html = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
