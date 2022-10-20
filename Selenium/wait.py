from selenium import webdriver
from selenium.webdriver.chrome.

driver = webdriver.Chrome()

PATH = "https://google.com"


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.ID, "main")
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header)
finally:
    driver.quit()
