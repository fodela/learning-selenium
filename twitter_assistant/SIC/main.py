import os
from selenium import webdriver

from pages import TwitterHomePage

PATH = "/usr/local/bin/chromedriver"
os.chmod(PATH, 755)

driver = webdriver.Chrome(PATH)


def post_a_tweet():
    try:
        twitter = driver.get("https://twitter.com/home")
        twitter_home_page = TwitterHomePage(driver)
    finally:
        # driver.close()
        pass


if __name__ == "__main__":
    post_a_tweet()
