import allure
import pytest
import time

from selenium import webdriver

@allure.title("Dry run of the Framework")
@allure.description("Verify that the dry run is working")
@allure.feature("TC#1- Sample Test run")
@pytest.mark.sample
def test_sample():
    print("Hello Sample")
    assert True==True

@allure.title("Dry run of the Framework 2")
@allure.description("Verify that the dry run is working")
@allure.feature("TC#2- Sample failed Test run")
@pytest.mark.sample
def test_sample_fail():
    print("Hello Sample")
    assert True==False