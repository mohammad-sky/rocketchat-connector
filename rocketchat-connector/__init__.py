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
        
    def find_by_username(self, username):
        """find_user_by_name ()
        locate existing contact by username or number
        Args:
            username ([type]): [description]
        """
        try:
            Find_the_search_mark = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[2]/aside/div[1]/div/div/div[2]/button[2]/i')))
            Find_the_search_mark.click()
            
            
            search_box = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[2]/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input')))
            search_box.clear()
            search_box.send_keys(username)
            search_box.send_keys(Keys.ENTER)
        except Exception as bug:
            error = f'Exception raised while finding user {username}\n{bug}'
            print(error)
            
            
    def send_message(self, message):
        """send_message ()
        Sends a message to a target user
        Args:
            message ([type]): [description]
        """
        try:
            inp_xpath = '/html/body/div[1]/div[2]/div[2]/div/main/div/div/div/div/div/section/div/div/footer/div/label/textarea'
            input_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, inp_xpath)))
            input_box.send_keys(message + Keys.ENTER)
        except (NoSuchElementException, Exception) as bug:
            print(bug)

        finally:
            print("send_message() finished running ")
            
