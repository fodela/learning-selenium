
from locators import TwitterHomePageLocator


class BasePage():
    def __init__(self, driver) -> None:
        self.driver = driver


class TwitterHomePage(BasePage):
    def type_tweet(self, tweet: str):
        twitter_post_box = self.driver.find_element(
            *TwitterHomePageLocator.TWITTER_POST_BOX)

    def click_tweet_button(self, type: str) -> None:
        tweet_button = self.driver.find_element(
            *TwitterHomePageLocator.TWEET_BUTTON)
