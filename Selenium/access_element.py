import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "__path_placeholder"

driver = webdriver.Chrome(PATH)

driver.get("https://google.com")

page_title = driver.title
print(page_title)


# access element => driver.find_element
# specific way of accessing element find_element.specific way. specific_element  => _by_id, _by_name, _by_class etc...
search_field = driver.find_element_by_name("s")

search_field.send_keys("test")
search_field.send_keys(Keys.RETURN)

# get whole website source code
source_code = driver.page_source
print(source_code)

time.sleep(5)

driver.quit()
