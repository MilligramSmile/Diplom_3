import allure
import data

from selenium.webdriver import ActionChains
from conftest import driver,user_data
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage

class TestOrderPage:
    @allure.title("Процесс оформления заказа")
    @allure.description(
        "Этот тест проверяет что залогиненный пользователь может оформить заказ")
    def test_constructor_button(self, driver,user_data):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(data.Urls.LOGIN_PAGE)
        email, password = user_data
        personal_account_page.input_email(email)
        personal_account_page.input_password(password)
        personal_account_page.click_login_button()
        main_page = MainPage(driver)
        button = main_page.find_button_create_order()
        assert button is not None

    @allure.description(
        "Этот тест проверяет что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.STELLAR_BURGERS)
        bun_element = main_page.find_ingredient_bun()
        drop_area = main_page.find_space_to_add_ingredient()
        actions = ActionChains(driver)
        actions.drag_and_drop(bun_element, drop_area).perform()
        counter = main_page.find_counter_bun()
        assert counter.text == '2'
