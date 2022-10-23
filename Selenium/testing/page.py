from selenium import webdriver
from elements import BasePageElement

from Selenium.testing.locators import MainPageLocators
# Base page


class SearchTextElement(BasePageElement):
    pass


class BasePage():
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

# Main page


class MainPage(BasePage):
    # check title
    def is_keyword_in_title(self, keyword: str) -> bool:
        return keyword in self.driver.title

    def click_go_button(self) -> None:
        go_button = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        go_button.click()


class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found" not in self.page_source
