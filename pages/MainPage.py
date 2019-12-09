import allure
import pytest
from selenium.webdriver.common.by import By
from utils.BasePage import BasePage


class MainPage(BasePage):
    BTN_ENTER = (By.XPATH, '//a[contains(@ga-event-action, "sign in")]')
    FIELD_EMAIL = (By.XPATH, '//input[contains(@type, "email")]')
    BTN_NEXT = (By.XPATH, '//div[@id="identifierNext"]')
    FIELD_PASSWORD = (By.NAME,  "password")
    HEADER_AUTH = (By.XPATH, '//div[@id="profileIdentifier"]')
    BTN_NEXT_PASSWORD = (By.XPATH, '//div[@id="passwordNext"]')
    BTN_SHOW_PASSWORD = (By.XPATH, '//div[@data-tooltip="Показать пароль"]')
    TITLE_LETTERS = (By.XPATH, '//title')



    @allure.step('Authorization with akordyukova.pronto#gmail.com/qwer123ASD!')
    def authorise(self):
        self.fill_field('akordyukova.pronto@gmail.com', MainPage.FIELD_EMAIL)
        self.click_element(MainPage.BTN_NEXT)
        self.assert_element_text(MainPage.HEADER_AUTH, "akordyukova.pronto@gmail.com")
        self.click_element(MainPage.BTN_SHOW_PASSWORD)
        element = self.driver.find_element_by_name("password")
        element.send_keys("qwer123ASD!")
        self.click_element(MainPage.BTN_NEXT_PASSWORD)


