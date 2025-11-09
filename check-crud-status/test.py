import pandas as pd
from selenium import webdriver
from modules import change_language, dashboard, logout, generic_pages, find_buttons, check_links, navigate_dashboard, login_driver

options = {
    "1": "Check all links",
    "2": "Change language pages",
    "3": "Dashboard pages",
    "4": "Logout page",
    "5": "Generic pages",
    "6": "Find buttons"
}

for k, v in options.items():
    print(f"{k}. {v}")

choice = input("Enter option number: ").strip()

driver = webdriver.Chrome()
login_driver.login(driver)
df = pd.read_csv("internal_links.csv")

if choice == "1":
    check_links.check_links(driver)
elif choice == "2":
    sub_choice = input("1: Switch to specific language, 2: Check all languages: ").strip()
    if sub_choice == "1":
        lang_num = input("Enter language number: ").strip()
        change_language.switch_to_language(driver, lang_num)
    elif sub_choice == "2":
        change_language.check_all_languages(driver)
elif choice == "3":
    navigate_dashboard.handle(driver)
elif choice == "4":
    logout.handle(driver)
elif choice == "5":
    for _, row in df.iterrows():
        link = row["Internal Link"]
        status = str(row["Status"]).lower()
        if "report" in link or "employee" in link or "settings" in link:
            driver.get(f"https://bxvfe.hrm.clickspikes.com/{link}")
            generic_pages.handle(driver, link, status)
elif choice == "6":
    for _, row in df.iterrows():
        link = row["Internal Link"] 
        if any(x in link for x in ["change-language/", "home", "dashboard", "dashboard#!"]):
            continue
        driver.get(link)
        find_buttons.scan(driver, link)

driver.quit()
