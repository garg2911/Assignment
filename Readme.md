
# Selenium 

Selenium is a Python library for dealing with Selenium keywords

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install webdriver-manager.

```bash
pip install webdriver-manager
pip install selenium 
```

## Usage

```python
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
