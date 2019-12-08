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
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()

@pytest.fixture
def selenium(selenium):
    driver = webdriver.Chrome
    driver.maximize_window()
    return driver
    # selenium.implicitly_wait(10)
    # selenium.maximize_window()
    # return selenium

@pytest.fixture(scope="session")
def base_fixture():
    config = configparser.ConfigParser()
    config.read(config_name)
    return config

@pytest.fixture()
def token(request):
    URL = request['services']['single_auth']
    headers = {'Content-Type': 'application/json'}
    date = {"setCookie": True,
            "username": request['base']['login'],
            "password": request['base']['password']
            }
    response = requests.post(url=URL + '/v1/login', data=json.dumps(date))
    token = response.json()['token']
    return token


# with open(config_name) as f:
#     sample_config = f.read()
# conf = configparser.RawConfigParser(allow_no_value=True)