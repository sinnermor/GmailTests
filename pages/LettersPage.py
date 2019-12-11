import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage


class LettersPage(BasePage):

    BTN_WRITE = (By.XPATH, '//div[text()="Написать"]')
    HEADER_NEW_MESSAGE = (By.XPATH, '//div[text()="Новое сообщение"]')
    FIELD_TO = (By.XPATH, '//textarea[contains(@name, "to")]')
    BTN_COPY = (By.XPATH, '//span[text()="Копия"][1]')
    BTN_HIDDEN_COPY = (By.XPATH, '//span[text()="Скрытая копия"]')
    FIELD_SUBJECT = (By.XPATH, '//input[@name="subjectbox"]')
    FIELD_BODY = (By.XPATH, '//div[@aria-label="Тело письма"]')
    BTN_SEND = (By.XPATH, '//div[contains(@data-tooltip,"Отправить")]')
    POPUP_SENDED_MESSAGE = (By.XPATH, '//span[text()="Письмо отправлено."]')

    TABLE_MESSAGES = (By.XPATH, '//table/tbody/tr[contains(@aria-labelledby, ":2m")]/td')
    TABLE_MESSAGE_SENDER = (By.XPATH, '//div[contains(@role,"tabpanel")]/div/div/table/tbody/tr[1]/td[5]')
    TABLE_MESSAGE_BODY_THEME = (By.XPATH,
                                '//tr[1]/td[6]/div/div/div/span[@class="bog"]/span')
    TABLE_MESSAGE_BODY = (By.XPATH, '//div[contains(@role,"tabpanel")]/div/div/table/tbody/tr[1]/td[6]/div/div/span')

    @allure.step('')
    def send_message(self):
        element = self.find_element(self.BTN_SEND)
        element.click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(self.POPUP_SENDED_MESSAGE),
                                               message="Can't find elements by locator", )
