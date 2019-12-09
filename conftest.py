import pytest
import requests
import json
import os
# from api.client import RestfulBookerClient
import configparser
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

config_name = 'conf.cfg'

@pytest.fixture(scope="session")
def chrome_driver(request):
    driver = webdriver.Chrome("chromedriver")
    return driver

@pytest.fixture()
def selenium():
    driver = webdriver.Chrome
    yield driver
    driver.quit()
