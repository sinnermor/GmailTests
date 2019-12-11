import allure
import pytest
from selenium import webdriver

import logging
from pages.MainPage import MainPage

config_name = 'conf.cfg'



@pytest.fixture(scope= "function")
def authorise(remote_chrome):
    auth_page = MainPage(remote_chrome)
    auth_page.go_to_site()
    auth_page.authorise()
    return  authorise

@pytest.fixture(scope='function')
def remote_chrome(request):
    # driver = webdriver.Remote(command_executor="http://hub:4444/wd/hub", desired_capabilities={'browserName': 'chrome', 'platformName': 'LINUX'})
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_window_size(1920, 1080)
    def fin():
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, attachment_type=allure.attachment_type.PNG)
        logging.info("Closing webdriver instance")
        driver.quit()

    yield driver
    request.addfinalizer(fin)

@pytest.fixture(scope='module')
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(15)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    def fin():
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, attachment_type=allure.attachment_type.PNG)
        logging.info("Closing webdriver instance")
        driver.quit()
    yield driver
    request.addfinalizer(fin)

