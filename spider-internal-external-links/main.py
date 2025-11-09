from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from urllib.parse import urljoin, urlparse
import time

driver = webdriver.Chrome()
base_url = 'https://bxvfe.hrm.clickspikes.com/login'
driver.get(base_url)
time.sleep(2)

email_input = driver.find_element(By.NAME, 'email')
password_input = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

email_input.send_keys('mdsameersayed0@gmail.com')
password_input.send_keys('Sam12#eer')
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

df_internal = pd.DataFrame(list(internal_links), columns=['Internal Link'])
df_external = pd.DataFrame(list(external_links), columns=['External Link'])
df_internal.to_csv('links/internal_links.csv', index=False)
df_external.to_csv('links/external_links.csv', index=False)

driver.quit()
