# Selenium

#### Content

Overview

### Prerequisites

1. Ensure you have chrome browser or firefox browser installed on your computer. Here I am using chrome.

2. Set up your virtual environment
   replace my_env_name with the name of your virtual environment

```bash
python3 -m venv my_env_name
```

````bash
python -m venv my_env_name

## Getting Started

Install selenium

```bash
pip install selenium
````

OR

```bash
pip3 install selenium
```

OR

```bash
python3 -m pip install selenium
```

<!-- FIXME -->

Install web driver
You can install either [Chrome webdriver]() or [firefox webdriver]()

#### Open and close tabs

```python
from selenium import webdriver
```

1. set up the driver

```python

    PATH = "path_to_where_you_downloaded_the_webdriver"
   driver = webdriver(PATH)
```

2. Open a webpage

```python
website_url = "https//:www.google.com"
driver.get(website_url)
```

3. Close the current browser tab

```python
driver.close()
```

4. Close the browser window

```python
driver.quit()
```

### Accessing attribute and elements of a webpage

**Attributes**

Title

```python
title = driver.title
```

Source code

```python
source_code = driver.page_source
```

Note: There are many more attributes and typing `driver.` will give you a list of attribute as autocompletion options.

Elements can be accessed by:

- id with `By.ID`
- name with `NAME`
- xpath with `XPATH`
- css_selector with `CSS_SELECTOR`

We must first import By

```python
from selenium.webdriver.common.by import by
```

```python
from selenium.common import By
```

1. Get a single element
2. `find_element: (by: str = By.ID, value: Any | None = None) -> WebElement`

```python
from selenium import By
   # syntax
   element = find_element(by, value)

   #e.g
   search_box = find_element(By.ID, "searchID")

```

Get a list of elements
`find_elements: (by: str = By.ID, value: Any | None = None) -> WebElement`

```python
from selenium import By
   # syntax
   elements = find_elements(by, value)

   #e.g
   all_buttons = find_element(By.TAG_NAME, "button")

```

### Interacting with the page

#### By keyboard

We import Keys for "keyboard" from selenium.webdriver.common.KEYS

To press the keyboard we use the method `send_keys: value: Any -> None`

#### Using the mouse

Click

```python
element.click()
```

### Navigation

Going back

```python
driver.back()
```

Going forward

```python
driver.forward()
```

### Action Chains

Enable a predefine number of actions that will only be performed

```python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
action.click()
action.perform()
```

### Wait

- **Implicitly wait** Waits for a number of time before executing the next line of code

```python
# implicitly_wait: secs: int -> None
driver.implicitly_wait(5)
```

- **WebDriverWait**: waits for a number of seconds until an element is on the page.

```python
from selenium.webdriver.support.ui import WebDriverWait

```

### OOP approach

Objects:

1. Pages
2. Elements
3. Locators

**Pages**
Has the following objects:

1. Base page: this page has attributes that all other pages inherit from

```python
class BasePage():
   def __init__(self, driver)-> None:
      self.driver = driver
```

2. Customized pages
   They inherit from the BasePage
   They have methods that perform specific things on the page.

   ```python
   class HomePage(BasePage):
      def is_title_matches(self, title_keyword: str) -> bool:
         return title_keyword in self.driver.title
   ```

**Elements**
This object has methods that set and get element on the page. We can think of it as a blueprint for setting and getting element.

```python
from selenium.webdriver.support.ui import WebdriverWait
class BasePageElement():
   def __set__(self, obj, value):
      WebDriverWait(driver, 100).until(
         lambda driver: driver.find_element_by_name(self.locator)
      )
```

**Locators**
Predefine locators to prevent repetition DRY principles.
