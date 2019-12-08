

class TableHelper:

    def __init__(self, driver, locator):
        self.driver = driver
        element = driver.find_element(by=locator)

