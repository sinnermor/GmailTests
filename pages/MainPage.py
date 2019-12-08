import allure
import pytest
from selenium.webdriver.common.by import By
from utils.BasePage import BasePage


class MainPage(BasePage):
    BTN_ENTER = (By.XPATH, '//a[contains(@ga-event-action, "sign in")]')
    FIELD_EMAIL = (By.XPATH, '//input[contains(@type, "email")]')
    BTN_NEXT = (By.XPATH, '//div[@id="identifierNext"]')
    FIELD_PASSWORD = (By.XPATH, '//input[contains(@name, "password")]')
    BTN_NEXT_PASSWORD = (By.XPATH, '//div[@id="passwordNext"]')

    BTN_WRITE = (By.XPATH, '//div[text()="Написать"]')
    HEADER_NEW_MESSAGE = (By.XPATH, '//div[text()="Новое сообщение"]')
    FIELD_TO = (By.XPATH, '//textarea[contains(@name, "to")]')
    BTN_COPY = (By.XPATH, '//span[text()="Копия"][1]')
    BTN_HIDDEN_COPY = (By.XPATH, '//span[text()="Скрытая копия"]')
    FIELD_SUBJECT = (By.XPATH, '//input[@name="subjectbox"]')
    FIELD_BODY = (By.XPATH, '//div[@aria-label="Тело письма"]')
    BTN_SEND = (By.XPATH, '//div[contains(@data-tooltip,"Отправить")]')

    TABLE_MESSAGES = (By.XPATH, '//table/tbody/tr[contains(@aria-labelledby, ":2m")]/td')
    TABLE_MESSAGE_SENDER = (By.XPATH, '//table/tbody/tr[contains(@aria-labelledby, ":2m")]/td[5]')
    TABLE_MESSAGE_BODY_THEME = (By.XPATH,
                                '//table/tbody/tr[contains(@aria-labelledby, ":2m")]/td[6]/div/div/div/span/span')
    TABLE_MESSAGE_BODY = (By.XPATH, '//table/tbody/tr[contains(@aria-labelledby, ":2m")]/td[6]/div/div/span')

    @allure.step('Authorization with akordyukova.pronto#gmail.com/qwer123ASD1')
    def authorise(self):
        self.fill_field('akordyukova.pronto@gmail.com', MainPage.FIELD_EMAIL)
        self.click_element(MainPage.BTN_NEXT)
        self.fill_field('qwer123ASD!', MainPage.BTN_NEXT_PASSWORD)
        self.click_element(MainPage.BTN_NEXT_PASSWORD)


