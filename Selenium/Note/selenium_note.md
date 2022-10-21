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
