import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage



class LoginPage(BasePage):

    @allure.step('Нажимаем на кнопку Восстановить пароль')
    def click_recover_password_button(self):
         self.click_element(LoginPageLocators.RECOVER_PASSWORD)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_recover_button(self):
        self.wait_and_find_element(LoginPageLocators.BUTTON_RECOVER)
        self.click_element(LoginPageLocators.BUTTON_RECOVER)

    @allure.step('Ввод почты')
    def input_email(self, name):
        self.wait_and_find_element(LoginPageLocators.INPUT_EMAIL).send_keys(name)

    @allure.step('Нажать на кнопку скрыть пароль')
    def click_hover_button(self):
        self.wait_and_find_element(LoginPageLocators.HOVER_PASSWORD_BUTTON)
        self.click_element(LoginPageLocators.HOVER_PASSWORD_BUTTON)

    @allure.step('Нажать на кнопку Сохранить')
    def find_button_saved(self):
        return self.wait_and_find_element(LoginPageLocators.BUTTON_SAVED)

    @allure.step('Поле пароль активно')
    def find_input_password_active(self):
        return self.wait_and_find_element(LoginPageLocators.PASSWORD_INPUT_ACTIVE)
