from selenium import webdriver


class BasePage():
    def __init__(self) -> None:
        self.driver = webdriver


class TwitterHomePage(BasePage):
    def type_tweet(self, tweet: str):
        pass

    def click_tweet_button(self) -> None:
        tweet_button = self.driver.find_element(
            *TwitterHomePageLocators.TWEET_BUTTON)
        tweet_button.click()
