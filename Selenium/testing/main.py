import os
import unittest
import page
from selenium import webdriver


PATH = "/usr/local/bin/chromedriver"
os.chmod(PATH, 755)

URL = "http://www.python.org"


class PythonOrgSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(URL)

    def test_search_in_python_org(self):
        main_page = page.MainPage(self.driver)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
