import allure
import pytest

from pages.LettersPage import LettersPage
from pages.MainPage import MainPage
from utils.BasePage import BasePage as page
from selenium.webdriver.common.by import By


class TestSuit:


    message_params = [('akordyukova.pronto@gmail.com','piu','test'), ('akordyukova.pronto@gmail.com','test','test')]
    @pytest.mark.parametrize('to, theme, body', message_params)
    @allure.feature("Проверка отправки писем")
    def test_message_send(self, chrome_driver, authorise, to, theme, body):
        letters_page = LettersPage(chrome_driver)
        page.click_element(letters_page, letters_page.BTN_WRITE)
        page.fill_field(letters_page, to, letters_page.FIELD_TO)
        page.fill_field(letters_page, theme, letters_page.FIELD_SUBJECT)
        page.fill_field(letters_page, body, letters_page.FIELD_BODY)
        page.click_element(letters_page, letters_page.BTN_SEND)
        page.assert_element_text(letters_page, letters_page.TABLE_MESSAGE_SENDER, "я")
        page.assert_element_text(letters_page, letters_page.TABLE_MESSAGE_BODY, body)