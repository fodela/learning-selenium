from selenium.webdriver.common.by import By


class MainPageLocators():
    GO_BUTTON = (By.ID, "submit")


# class MainPageLocator():
#     def __init__(self, condition: str, locator_name: str) -> None:
#         self.condition = condition
#         self.locator_name = locator_name

#     def set_locator(self) -> None:
#         if self.condition == "id":
#             ELEMENT = (By.ID, self.locator_name)
