import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
load_dotenv()


sleep(5)
url = os.environ.get("URL")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=chrome_options.to_capabilities())

driver.implicitly_wait(os.environ.get("WAIT_IN_SECONDS"))
print('\x1b[6;30;42m' + "URL Value is, " + "\033[0m" + url)
driver.get(url)

