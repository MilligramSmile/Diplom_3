from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import  allure


class PersonalAccountPage(BasePage):
    @allure.step('Заполняем поле Email')
    def input_email(self, email):
        self.wait_and_find_element(PersonalAccountPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step('Заполняем поле Пароль')
    def input_password(self, password):
        self.wait_and_find_element(PersonalAccountPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Нажимаем на кнопку Войти')
    def click_login_button(self):
        self.wait_and_find_element(PersonalAccountPageLocators.LOGIN_BUTTON)
        self.click_element(PersonalAccountPageLocators.LOGIN_BUTTON)

    @allure.step('Нажимаем на кнопку Выйти')
    def click_logout_button(self):
        self.wait_and_find_element(PersonalAccountPageLocators.LOGOUT_BUTTON)
        self.click_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Нажимаем на кнопку Личный Кабинет')
    def click_header_login_button(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Нажимаем на кнопку История заказов')
    def click_button_order_history(self):
        self.wait_and_find_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
        self.click_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Находим кнопку Оформить заказ')
    def find_create_order_button(self):
        return self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Находим номер заказа')
    def find_order_number(self):
        return self.wait_and_find_element(PersonalAccountPageLocators.ORDER_HISTORY_ITEM_NUMBER)

    @allure.step('Находим на кнопку Выйти')
    def find_logout_button(self):
        return self.wait_and_find_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Находим заголовок Соберите бургер')
    def find_collect_burger(self):
        return self.wait_and_find_element(MainPageLocators.COLLECT_BURGER)

    @allure.step('Находим кнопку Восстановить пароль')
    def find_recover_password(self):
        return self.wait_and_find_element(LoginPageLocators.RECOVER_PASSWORD)
