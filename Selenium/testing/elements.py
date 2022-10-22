from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement():
    def __set__(self, obj, value):
        driver = obj.driver
        # Wait for 100 seconds until the search box is on the
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        # Clear the search box
        driver.find_element_by_name(self.locator).clear()
        # fill the search box
        driver.find_element_by_name(self.locator).send_keys_value
