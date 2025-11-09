import pandas as pd
import time
from datetime import datetime
from selenium.common.exceptions import WebDriverException

def handle(driver, csv_path="internal_links.csv", output_path="../logs/dashboard_log.csv"):
    df = pd.read_csv(csv_path)
    targets = df[df["Internal Link"].str.contains("dashboard|home", case=False, na=False)]
    logs = []

    for _, row in targets.iterrows():
        link = str(row["Internal Link"]).strip()
        #full_url = f"https://bxvfe.hrm.clickspikes.com/{link}"
        status = "FAIL"
        start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            driver.get(link)
            time.sleep(2)
            if driver.current_url.startswith("https://bxvfe.hrm.clickspikes.com"):
                status = "OK"
        except WebDriverException:
            status = "FAIL"

        logs.append({"Link": link, "Visited": start, "Status": status})
        print(f"{link} -> {status}")

    pd.DataFrame(logs).to_csv(output_path, index=False)
    print(f"\nDashboard visit log saved to {output_path}")
