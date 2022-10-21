import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://newtoxic.com/new/1/Videos/TV-Series/The-IT-Crowd.html"

# load_dotenv()

# PATH = os.getenv("PATH")
PATH = "/usr/local/bin/chromedriver"
os.chmod(PATH, 755)

driver = webdriver.Chrome(PATH)

driver.get(URL)

try:
    seasons = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "ul"))
    )
    seasons = driver.find_element(By.TAG_NAME, "ul")

    seasons_list = seasons.find_elements(By.TAG_NAME, "a")

    # print(seasons)
    for season in seasons:
        print("######", season.text, "\n")
        # season.click()

except Exception as e:
    print(f"This error happened! =>>> {e}")

finally:
    driver.close()
