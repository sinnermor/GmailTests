import pytest

from pages.MainPage import MainPage
from utils.BasePage import BasePage as page
from selenium.webdriver.common.by import By


def test_gui_base(driver):
    auth_page = MainPage(driver)
    auth_page.go_to_site()
    auth_page.authorise()

message_params = [('akordyukova.pronto@gmail.com','','test'), ('akordyukova.pronto@gmail.com','test','test')]
@pytest.mark.parametrize('to, theme, body', message_params)
def test_message_send(driver, to, theme, body):
    auth_page = MainPage(driver)
    auth_page.go_to_site()
    auth_page.authorise()
    page.click_element(auth_page, MainPage.BTN_WRITE)
    page.fill_field(auth_page, to, MainPage.FIELD_TO)
    page.fill_field(auth_page, theme, MainPage.FIELD_SUBJECT)
    page.fill_field(auth_page, body, MainPage.FIELD_BODY)
    page.click_element(auth_page, MainPage.BTN_SEND)
    # elements = driver.find_elements(by=MainPage.TABLE_MESSAGES)
    page.assert_element_text(auth_page, MainPage.TABLE_MESSAGE_SENDER, "я")
    page.assert_element_text(auth_page, MainPage.TABLE_MESSAGE_BODY_THEME, "(без темы)")
    page.assert_element_text(auth_page, MainPage.TABLE_MESSAGE_BODY, "test")