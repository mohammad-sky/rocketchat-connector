import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)
from webdriver_manager.chrome import ChromeDriverManager


class rocket_connector(object):
    def __init__(self, browser = None):
        self.BASE_URL = 'your rocket chat URl'
        if not browser:
            browser = webdriver.Chrome(
                ChromeDriverManager().install(),
                options=self.chrome_options,
            )

        self.browser = browser

        self.wait = WebDriverWait(self.browser, 600)
        self.login()
        
    @property
    def chrome_options(self):
        chrome_options = Options()
        if sys.platform == "win32":
            chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument(
                '--user-data-dir=C:/Temp/ChromeProfile')
        else:
            chrome_options.add_argument("start-maximized")
            chrome_options.add_argument('--user-data-dir=./User_Data')
        return chrome_options

    def login(self):
        self.browser.get(self.BASE_URL)
        self.browser.maximize_window()
