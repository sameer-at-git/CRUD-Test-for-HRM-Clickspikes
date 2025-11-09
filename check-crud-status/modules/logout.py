from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import pandas as pd
import time
from datetime import datetime

def handle(driver, output_path="../logs/logout_log.csv"):
    logs = []
    dashboard_link = "https://bxvfe.hrm.clickspikes.com/dashboard"
    driver.get(dashboard_link)
    time.sleep(2)
    
    status = "FAIL"
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        dropdown = driver.find_element(By.CSS_SELECTOR, "a.dash-head-link.dropdown-toggle")
        dropdown.click()
        time.sleep(1)
        
        logout_btn = driver.find_element(By.XPATH, "//a[contains(@href, '/logout')]")
        logout_btn.click()
        time.sleep(3)
        
        if "https://bxvfe.hrm.clickspikes.com/" in driver.current_url:
            status = "OK"
        else:
            status = "FAIL"
            
    except (NoSuchElementException, WebDriverException) as e:
        status = "FAIL"
        print(f"Error during logout: {e}")
    
    logs.append({"Action": "Logout", "Visited": start_time, "Status": status})
    pd.DataFrame(logs).to_csv(output_path, index=False)
    
    print(f"Logout -> {status}")
    print(f"Logout log saved to {output_path}")
