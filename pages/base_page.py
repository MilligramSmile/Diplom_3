from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_element_to_disappear(self, locator):
        WebDriverWait(self.driver, 15).until(ec.invisibility_of_element_located(locator))
        return True

    def is_text_present(self, text):
        return text in self.driver.page_source



