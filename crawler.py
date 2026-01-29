import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configuration
PROXY = os.getenv("PROXY_URL")
OUTPUT_DIR = "/data/html_pages"

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    if PROXY:
        chrome_options.add_argument(f'--proxy-server={PROXY}')

    return webdriver.Chrome(options=chrome_options)

def crawl():

    driver = setup_driver()
    count = 0
    page_num = 1

    try:
        while count < 201:
            print(f"Exploration de la liste page {page_num}...")
            driver.get(f"https://www.carzone.ie/search?page={page_num}")



            
            try:
                time.sleep(2) 
                
                html_source = driver.page_source
                file_path = os.path.join(OUTPUT_DIR,f"car_{count:03d}.html")
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(html_source)
                
                count += 1
                page_num+=1
                print(f"[{count}/200] Sauvegardé ")
            except Exception as e:
                print(f"Erreur sur : {e}")

        page_num += 1
    finally:
        driver.quit()

if __name__ == "__main__":
    crawl()