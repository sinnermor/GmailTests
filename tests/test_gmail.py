import allure
import pytest

from pages.LettersPage import LettersPage
from pages.BasePage import BasePage as page


@allure.suite("test")
class TestSuit:


    message_params = [('akordyukova.pronto@gmail.com','','test'), ('akordyukova.pronto@gmail.com','test','test')]
    @pytest.mark.parametrize('to, theme, body', message_params)
    @allure.story("Проверка отправки писем")
    def test_message_send(self, remote_chrome, authorise, to, theme, body):
        letters_page = LettersPage(remote_chrome)
        page.click_element(letters_page, letters_page.BTN_WRITE)
        page.fill_field(letters_page, to, letters_page.FIELD_TO)
        page.fill_field(letters_page, theme, letters_page.FIELD_SUBJECT)
        page.fill_field(letters_page, body, letters_page.FIELD_BODY)
        letters_page.send_message()
        page.assert_element_text(letters_page, letters_page.TABLE_MESSAGE_SENDER, "я")
        letters_page.check_theme(theme)
        page.assert_element_text(letters_page, letters_page.TABLE_MESSAGE_BODY, body)