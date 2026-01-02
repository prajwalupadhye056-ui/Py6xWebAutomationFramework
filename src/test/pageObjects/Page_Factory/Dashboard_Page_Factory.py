from seleniumpagefactory.Pagefactory import PageFactory
from src.test.utils.common_utils import *
from selenium.webdriver.common.by import By
import time

class DashboardPage(PageFactory):

    def __init__(self,driver):
        self.driver=driver
        self.highlight= True

locators={

            'username-logged_in':('XPATH',"//span[@data-qa='lufexuloga']")

        }


def user_logged_in_text(self):
   webdriver_wait_url(driver=self.driver,timeout=5)
   return self.username_logged_in.get_text()