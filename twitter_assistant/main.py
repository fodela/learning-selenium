import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# website = "https://www.adamchoi.co.uk/overs/detailed"
website = "https://www.youtube.com"
os.chmod("/usr/local/bin/chromedriver", 755)
path = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(path)
driver.get(website)
print(driver.page_source)
try:
    search_box = driver.find_element(By.ID, "search")
    print("search box is ", search_box)
    search_box.send_keys("fireship.io")
    search_box.send_keys(Keys.Return)
    driver.find_elements

finally:
    time.sleep(10)
    driver.close()
