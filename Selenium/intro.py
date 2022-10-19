# import webdriver from selenium
# from selenium import webdriver
import selenium

# define path of webdriver
PATH = "__path_placeholder"

# define driver
driver = selenium.webdriver

# Open webbrowser
driver.get("https://google.com")

# close current tab
driver.close()

# close the browser window
driver.quit()
