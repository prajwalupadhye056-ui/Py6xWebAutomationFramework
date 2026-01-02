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
from src.test.pageObjects.PageObjectModel.vwo.freeTrailPage import freeTrailPage

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


@allure.epic("VWO Free Trial")
@allure.description("TC#0 -VWO App Free Trial")
@allure.feature("TC#0 |VWO App Free Trial")
@pytest.mark.negative

def test_vwo_ft_negative(setup):
     driver=setup
     login_Page =LoginPage(driver=driver)
     login_Page.free_trial_button_click()


     take_screen_shot(driver=driver,name="test_vwo_ft_negative")
     free_trial_page=freeTrailPage(driver=driver)
     free_trial_page.enter_free_trial_details_invalid("admin")
     error_message_txt=free_trial_page.get_error_message_text()
     assert error_message_txt == "The email address you entered is incorrect."






