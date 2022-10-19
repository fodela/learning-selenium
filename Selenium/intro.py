# import webdriver from selenium
# from selenium import webdriver
import selenium

# define path of webdriver
PATH = "__path_placeholder"

# define driver
driver = selenium.webdriver.Chrome(PATH)

# Open webbrowser
driver.get("https://google.com")

# Get title of webpage
print(driver.title)

# close current tab
driver.close()

# close the browser window
driver.quit()
