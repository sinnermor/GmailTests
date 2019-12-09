import allure
import pytest
import requests
import json
import os
# from api.client import RestfulBookerClient
import configparser
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.MainPage import MainPage

config_name = 'conf.cfg'



@pytest.fixture(scope = "session")
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture(scope="session")
def authorise(chrome_driver):
    auth_page = MainPage(chrome_driver)
    auth_page.go_to_site()
    auth_page.authorise()

