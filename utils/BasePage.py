from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://gmail.com/"


    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")



    # def find_edit_element(self, locator, time=10):
    #     return WebDriverWait(self.driver, time).until(EC.element_to_be_selected())



    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def assert_element_text(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator,text))


    def go_to_site(self):
        return self.driver.get(self.base_url)

    def fill_field(self, text, locator):
        element = self.find_element(locator)
        self.driver.implicitly_wait(30)
        element.send_keys(text)
        return element

    def send_enter(self):
        self.driver.send_keys(Keys.ENTER)

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
        return element