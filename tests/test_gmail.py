import allure
import pytest

from pages.LettersPage import LettersPage
from pages.BasePage import BasePage as page


@allure.suite("test")
class TestSuit:
    message_params = [('akordyukova.pronto@gmail.com', '', 'test'), ('akordyukova.pronto@gmail.com', 'test', 'test')]

    @pytest.mark.parametrize('to, theme, body', message_params)
    @allure.story("Проверка отправки писем")
    def test_message_send(self, remote_chrome, authorise, to, theme, body):
        letters_page = LettersPage(remote_chrome)
        letters_page.click_element(letters_page.BTN_WRITE)
        letters_page.fill_field(to, letters_page.FIELD_TO)
        letters_page.fill_field(theme, letters_page.FIELD_SUBJECT)
        letters_page.fill_field(body, letters_page.FIELD_BODY)
        letters_page.send_message()
        page.assert_element_text(letters_page.TABLE_MESSAGE_SENDER, "я")
        letters_page.check_theme(theme)
        letters_page.assert_element_text(letters_page.TABLE_MESSAGE_BODY, body)

    message_params_errror = [('', 'test'), ('test', '')]

    @pytest.mark.parametrize('theme, body', message_params_errror)
    @allure.story("Проверка ошибки при незаполненом поле получателя")
    def test_message_send_error(self, remote_chrome, authorise, theme, body):
        letters_page = LettersPage(remote_chrome)
        letters_page.click_element(letters_page.BTN_WRITE)
        letters_page.fill_field(theme, letters_page.FIELD_SUBJECT)
        letters_page.fill_field(body, letters_page.FIELD_BODY)
        letters_page.click_element(letters_page.BTN_SEND)
        letters_page.find_element( letters_page.DIALOG_ALERT)

    message_params_copies = [('kordyukova.a@mail.ru', '', 'akordyukova.pronto@gmail.com', 'test'),
                             ('kordyukova.a@mail.ru', 'akordyukova.pronto@gmail.com', '', 'test')]

    @allure.story("Проверка получения сообщения как копия и скрытая копия")
    @pytest.mark.parametrize('to, copy, hidden_copy, body', message_params_copies)
    def test_copies(self, remote_chrome, authorise, to, copy, hidden_copy,  body):
        letters_page = LettersPage(remote_chrome)
        letters_page.click_element(letters_page.BTN_WRITE)
        letters_page.fill_field(to, letters_page.FIELD_TO)
        letters_page.click_element(letters_page.BTN_COPY)
        letters_page.fill_field(copy, letters_page.TEXTAREA_COPY)
        letters_page.click_element(letters_page.BTN_HIDDEN_COPY)
        letters_page.fill_field(hidden_copy, letters_page.TEXTAREA_HIDDEN_COPY)
        letters_page.fill_field(body, letters_page.FIELD_BODY)
        letters_page.send_message()
        letters_page.assert_element_text(letters_page.TABLE_MESSAGE_SENDER, "я")
        letters_page.assert_element_text(letters_page.TABLE_MESSAGE_BODY, body)
