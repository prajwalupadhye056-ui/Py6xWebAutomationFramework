import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os
from src.test.utils.Utils import *



@allure.title("VWO Login Negative TestCase")
@allure.description("TC#1- Negative TC -VWO Login with invalid credentials")
@allure.feature("VWO login with invalid credentials")
@pytest.mark.negativevwologin

def test_app_vwo_login_chrome():
    load_dotenv()
    match os.getenv("BROWSER"):
       case "chrome":
         chrome_options= Options()
         chrome_options.add_argument("--incognito")
         driver= webdriver.Chrome(chrome_options)

       case "Edge":
         edge_options = Options()
         edge_options.add_argument("--incognito")
         driver = webdriver.Edge(edge_options)

       case "Firefox":
         firefox_options = Options()
         firefox_options.add_argument("--incognito")
         driver = webdriver.Firefox(firefox_options)

       case _:
          print("Browser!!! not found")
          exit(1)

    driver.get(os.getenv("URL"))
    email_web_element= driver.find_element(By.ID,"login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    password_web_element = driver.find_element(By.ID, "password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    error_message_web_element=driver.find_element(By.CLASS_NAME,"notification")
    print(error_message_web_element.text)

    take_screen_shot(driver=driver,name="vwoLoginFailed")

    assert error_message_web_element.text ==os.getenv("error_message_expected")

    time.sleep(5)
    driver.quit()
