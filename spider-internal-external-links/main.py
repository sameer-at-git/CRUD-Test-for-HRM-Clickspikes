from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pandas as pd
from urllib.parse import urljoin, urlparse
import time, os

load_dotenv()
EMAIL = os.getenv("HRM_EMAIL")
PASSWORD = os.getenv("HRM_PASSWORD")

driver = webdriver.Chrome()
base_url = 'https://bxvfe.hrm.clickspikes.com/login'
driver.get(base_url)
time.sleep(2)

email_input = driver.find_element(By.NAME, 'email')
password_input = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
login_button.click()
time.sleep(5)

internal_links = set()
external_links = set()
elements = driver.find_elements(By.TAG_NAME, 'a')

for el in elements:
    href = el.get_attribute('href')
    if href:
        full_link = urljoin(base_url, href)
        if urlparse(full_link).netloc == urlparse(base_url).netloc:
            internal_links.add(full_link)
        else:
            external_links.add(full_link)

os.makedirs('links', exist_ok=True)
pd.DataFrame(list(internal_links), columns=['Internal Link']).to_csv('links/internal_links.csv', index=False)
pd.DataFrame(list(external_links), columns=['External Link']).to_csv('links/external_links.csv', index=False)

driver.quit()
