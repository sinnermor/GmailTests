from selenium.webdriver.common.by import By

from utils.BasePage import BasePage


class LettersPage(BasePage):

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
                                '//td[6]/div/div/div/span/span[1]')
    TABLE_MESSAGE_BODY = (By.XPATH, '//table/tbody/tr[contains(@aria-labelledby, ":2m")]/td[6]/div/div/span')