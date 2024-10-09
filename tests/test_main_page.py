import data
import allure

from conftest import driver
from pages.main_page import MainPage

class TestMainPage:

    @allure.title("Проверка основного функционала")
    @allure.description("Этот тест проверяет что происходит переход на Конструктор")
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.LOGIN_PAGE)
        main_page.click_constructor_button()
        main_page.find_collect_burger()
        assert main_page.get_current_url() == data.Urls.STELLAR_BURGERS

    @allure.description("Этот тест проверяет что происходит переход на Лента заказов")
    def test_order_tape_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.STELLAR_BURGERS)
        main_page.click_order_tape_button()
        main_page.find_order_tape()
        assert main_page.get_current_url() == data.Urls.ORDER_TAPE

    @allure.description(
        "Этот тест проверяет что если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.STELLAR_BURGERS)
        main_page.click_ingredient_bun()
        bun_info = main_page.find_ingredient_info()
        assert bun_info is not None

    @allure.description("Этот тест проверяет что всплывающее окно с деталями закрывается кликом по крестику")
    def test_close_ingredient_info(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.STELLAR_BURGERS)
        main_page.click_ingredient_bun()
        main_page.find_ingredient_info()
        main_page.click_ingredient_info_close()
        element = main_page.check_ingredient_info_disappear()
        assert element == True
