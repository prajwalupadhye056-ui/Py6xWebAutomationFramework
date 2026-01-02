import allure
import pytest
import time

#Assertions and use the Page Object class

#Webdriver start
#User Interaction  + Assertions
#Close Webdriver
from selenium import webdriver
from src.test.constants import constants
from src.test.constants.constants import Constants
from src.test.pageObjects.PageObjectModel.vwo.loginPage import LoginPage
from src.test.pageObjects.PageObjectModel.vwo.dashboardPage import  DashboardPage

from dotenv import load_dotenv
import os
from src.test.utils.Utils import *

@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver


@allure.epic("VWO Login Test")
@allure.description("TC#0 -VWO App Negative Test")
@allure.feature("TC#0 |VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
     driver=setup
     login_Page =LoginPage(driver=driver)
     login_Page.login_to_vwo(usr=os.getenv("INVALID_USERNAME"),pwd=os.getenv("INVALID_PASSWORD"))

     error_msg_element=login_Page.get_error_message_text()
     take_screen_shot(driver=driver,name="test_vwo_login_negative")
     assert error_msg_element == os.getenv("error_message_expected")


@allure.epic("VWO Login Test")
@allure.description("TC#0 -VWO App Positive Test")
@allure.feature("TC#0 |VWO App Positive Test")
@pytest.mark.negative
def test_vwo_login_positive(setup):
    driver=setup

    login_page= LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("USERNAME"), pwd=os.getenv("PASSWORD"))
    dashboard_page= DashboardPage(driver=driver)
    take_screen_shot(driver=driver, name="test_vwo_login_positive")
    assert os.getenv("USERNAME_LOGGED_IN")in dashboard_page.user_logged_in_text()


