from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime

load_dotenv()

EMAIL = os.getenv("HRM_EMAIL")
PASSWORD = os.getenv("HRM_PASSWORD")

def login(driver, output_csv="logs/login_log.csv"):
    driver.get("https://bxvfe.hrm.clickspikes.com")
    wait = WebDriverWait(driver, 10)
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "FAIL"

    try:
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")) )
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")) )
        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")) )

        email_input.clear()
        email_input.send_keys(EMAIL)
        password_input.clear()
        password_input.send_keys(PASSWORD)
        submit_btn.click()
        time.sleep(3)

        if "home" in driver.current_url.lower():
            status = "OK"

    except:
        status = "FAIL"

    try:
        df = pd.read_csv(output_csv)
    except:
        df = pd.DataFrame(columns=["timestamp", "email", "status"])

    new_row = pd.DataFrame([{"timestamp": start_time, "email": EMAIL, "status": status}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(output_csv, index=False)
