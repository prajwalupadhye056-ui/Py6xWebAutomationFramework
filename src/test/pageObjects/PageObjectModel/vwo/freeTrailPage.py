from selenium.webdriver.common.by import By

from src.test.utils.common_utils import webdriver_wait


class freeTrailPage:
    def __init__(self, driver):
        self.driver = driver

    username_email_ft = (By.XPATH, "//input[@id='page-v1-step1-email']")
    button_click_ft = (By.XPATH, "//button[normalize-space()='Create a Free Trial Account']")


def get_user_name_ft(self):
    return self.driver.find_element(*freeTrailPage.username_email_ft)


def get_button_click_ft(self):
    return self.driver.find_element(*freeTrailPage.button_click_ft)


