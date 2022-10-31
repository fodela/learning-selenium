from random import random
from selenium import webdriver
import os
import selenium

# define path of webdriver

PATH = "/usr/local/bin/chromedriver"
os.chmod(PATH, 755)

# define driver
driver = selenium.webdriver.Chrome(PATH)

# Open webbrowser


def attack(n):
    try:
        for i in range(n):
            driver.get("_placeholder")
            print(f"attacking {i}")

    except Exception as e:
        print("err -->", e)

    # finally:
    #     driver.close()


if __name__ == "__main__":

    attack(100000000000)
