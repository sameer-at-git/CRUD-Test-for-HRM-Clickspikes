import pandas as pd
import time

langs = {
    "1": ("Español", "change-language/es"),
    "2": ("Polish", "change-language/pl"),
    "3": ("Turkish", "change-language/tr"),
    "4": ("Russian", "change-language/ru"),
    "5": ("Italian", "change-language/it"),
    "6": ("German", "change-language/de"),
    "7": ("Chinese", "change-language/zh"),
    "8": ("Portuguese (Brazil)", "change-language/pt-br"),
    "9": ("Japanese", "change-language/ja"),
    "10": ("Arabic", "change-language/ar"),
    "11": ("Hebrew", "change-language/he"),
    "12": ("Danish", "change-language/da"),
    "13": ("French", "change-language/fr"),
    "14": ("English", "change-language/en"),
    "15": ("Dutch", "change-language/nl"),
    "16": ("Portuguese", "change-language/pt")
}

def switch_to_language(driver, language_number, csv_path="internal_links.csv"):
    df = pd.read_csv(csv_path)
    if language_number not in langs:
        print("Invalid option.")
        return
    selected = langs[language_number][1]
    match = df[df["Internal Link"].str.contains(selected, case=False, na=False)]
    if match.empty:
        print(f"No matching link found for {langs[language_number][0]}.")
        return
    link = match.iloc[0]["Internal Link"]
    print(f"Switching to {langs[language_number][0]} via {link}")
    driver.get(link)
    time.sleep(2)

def check_all_languages(driver, csv_path="internal_links.csv", log_csv="logs/language_log.csv"):
    df = pd.read_csv(csv_path)
    log_data = []
    langs = {
        "1": ("Español", "change-language/es"),
        "2": ("Polish", "change-language/pl"),
        "3": ("Turkish", "change-language/tr"),
        "4": ("Russian", "change-language/ru"),
        "5": ("Italian", "change-language/it"),
        "6": ("German", "change-language/de"),
        "7": ("Chinese", "change-language/zh"),
        "8": ("Portuguese (Brazil)", "change-language/pt-br"),
        "9": ("Japanese", "change-language/ja"),
        "10": ("Arabic", "change-language/ar"),
        "11": ("Hebrew", "change-language/he"),
        "12": ("Danish", "change-language/da"),
        "13": ("French", "change-language/fr"),
        "14": ("English", "change-language/en"),
        "15": ("Dutch", "change-language/nl"),
        "16": ("Portuguese", "change-language/pt")
    }

    for key, (name, path) in langs.items():
        match = df[df["Internal Link"].str.contains(path, case=False, na=False)]
        if match.empty:
            status = "not found"
            link = path
        else:
            link = match.iloc[0]["Internal Link"]
            try:
                driver.get(link)
                time.sleep(2)
                status = "OK"
                
            except:
                status = "FAIL"
        log_data.append({"language": name, "link": link, "status": status})

    pd.DataFrame(log_data).to_csv(log_csv, index=False)

