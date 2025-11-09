from selenium.webdriver.common.by import By
import time

def handle(driver):
    try:
        nav_links = driver.find_elements(By.CSS_SELECTOR, "a.nav-link")
        for nav in nav_links:
            nav.click()
            time.sleep(1)
    except:
        pass
