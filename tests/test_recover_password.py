import time

import data
import allure
from pages.login_page import LoginPage
from conftest import driver



class TestLoginButtons:

    @allure.title("Восстановление пароля")
    @allure.description(
        "Этот тест проверяет переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_header_order_button(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(data.Urls.LOGIN_PAGE)
        login_page.click_recover_password_button()
        assert login_page.get_current_url() == data.Urls.RECOVER_PASSWORD

    @allure.description("Этот тест проверяет ввод почты и клик по кнопке «Восстановить»")
    def test_confirm_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(data.Urls.RECOVER_PASSWORD)
        login_page.input_email(data.Login.EMAIL)
        login_page.click_recover_button()
        login_page.find_button_saved()
        assert login_page.get_current_url() == data.Urls.RESET_PASSWORD

#     клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
    @allure.description("Этот тест проверяет клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_hover_button(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(data.Urls.RECOVER_PASSWORD)
        login_page.input_email(data.Login.EMAIL)
        login_page.click_recover_button()
        time.sleep(2)
        login_page.find_button_saved()
        login_page.click_hover_button()
        password_input_active = login_page.find_input_password_active()
        assert password_input_active is not None




