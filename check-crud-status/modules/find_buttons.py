from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def scan(driver, page_url, output_csv="../logs/collected_links.csv"):
    wait = WebDriverWait(driver, 10)
    collected_links = []

    try:
        dash_content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dash-content")))
        body_links = dash_content.find_elements(By.TAG_NAME, "a")
        for a in body_links:
            href = a.get_attribute("href")
            if href and not any(x in href for x in ["change-language/", "home", "logout","dashboard", "dashboard#!"]):
                collected_links.append(href)
    except:
        pass

    if not collected_links:
        row_data = [page_url, "no links found"]
    else:
        row_data = [page_url] + collected_links

    try:
        df = pd.read_csv(output_csv)
    except:
        df = pd.DataFrame()

    new_row = pd.DataFrame([row_data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(output_csv, index=False, header=False)
