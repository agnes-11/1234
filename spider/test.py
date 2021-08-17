from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(options=options,executable_path=chromedriver)
driver.get("https://www.baidu.com")
print(driver.title)
driver.quit()
