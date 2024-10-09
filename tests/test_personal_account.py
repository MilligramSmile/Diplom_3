import allure
import data

from conftest import driver, user_data
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title("Личный кабинет")
    @allure.description("Этот тест проверяет переход по клику на «Личный кабинет»")
    def test_header_order_button(self, driver,user_data):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(data.Urls.LOGIN_PAGE)
        email, password = user_data
        personal_account_page.input_email(email)
        personal_account_page.input_password(password)
        personal_account_page.click_login_button()
        personal_account_page.find_collect_burger()
        personal_account_page.click_header_login_button()
        personal_account_page.find_logout_button()
        assert personal_account_page.get_current_url() == data.Urls.ACCOUNT_PAGE

    @allure.description("Этот тест проверяет переход в раздел «История заказов»")
    def test_order_history(self, driver,user_data):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(data.Urls.LOGIN_PAGE)
        email, password = user_data
        personal_account_page.input_email(email)
        personal_account_page.input_password(password)
        personal_account_page.click_login_button()
        personal_account_page.find_collect_burger()
        personal_account_page.click_header_login_button()
        personal_account_page.find_logout_button()
        personal_account_page.click_button_order_history()
        assert personal_account_page.get_current_url() == data.Urls.ORDER_HISTORY

    @allure.description("Этот тест проверяет выход из аккаунта")
    def test_logout_button(self, driver,user_data):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(data.Urls.LOGIN_PAGE)
        email, password = user_data
        personal_account_page.input_email(email)
        personal_account_page.input_password(password)
        personal_account_page.click_login_button()
        personal_account_page.find_collect_burger()
        personal_account_page.click_header_login_button()
        personal_account_page.click_logout_button()
        personal_account_page.find_recover_password()
        assert personal_account_page.get_current_url() == data.Urls.LOGIN_PAGE
