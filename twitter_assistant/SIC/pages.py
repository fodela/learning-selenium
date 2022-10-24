from selenium import webdriver

import locators


class BasePage():
    def __init__(self) -> None:
        self.driver = webdriver


class TwitterHomePage(BasePage):
    def type_tweet(self, tweet: str):
        pass

    def click_tweet_button(self, type: str) -> None:
        locator = locators.TwitterHomePageLocator(type, "elemento")
        # tweet_button = self.driver.find_element(
        # *locator.element)
        # tweet_button.click()
        print(locator.element)


if __name__ == "__main__":
    program = TwitterHomePage()
    program.click_tweet_button("name")
