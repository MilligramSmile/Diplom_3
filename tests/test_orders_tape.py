import pytest
import allure
import data
import time

from selenium.webdriver import ActionChains
from conftest import driver,user_data
from locators.feed_locators import FeedPageLocators
from pages.main_page import MainPage
from pages.orders_tape_page import OrderTapePage
from pages.personal_account_page import PersonalAccountPage


class TestOrderTapePage:

    @allure.title("Раздел «Лента заказов»")
    @allure.description("Этот тест проверяет если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_info(self, driver):
            order_tape_page = OrderTapePage(driver)
            order_tape_page.open_page(data.Urls.ORDER_TAPE)
            order_tape_page.click_order_item()
            order_modal = order_tape_page.find_order_info()
            assert order_modal is not None

    @allure.description(
        "Этот тест проверяет что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»"
    )
    def test_check_order_in_history(self, driver, user_data):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(data.Urls.LOGIN_PAGE)
        email, password = user_data
        # Логин
        personal_account_page.input_email(email)
        personal_account_page.input_password(password)
        personal_account_page.click_login_button()
        time.sleep(2)

        # Создаём новый заказ
        main_page = MainPage(driver)
        main_page.find_collect_burger()
        bun_element = main_page.find_ingredient_bun()
        drop_area = main_page.find_space_to_add_ingredient()
        actions = ActionChains(driver)
        actions.drag_and_drop(bun_element, drop_area).perform()
        time.sleep(2)
        main_page.click_button_create_order()
        time.sleep(5)
        main_page.click_ingredient_info_close()

        # time.sleep(10)
        # Переход в личный кабинет
        personal_account_page.click_header_login_button()
        personal_account_page.click_button_order_history()
        time.sleep(10)
        order_number = personal_account_page.find_order_number().text

        order_tape_page = OrderTapePage(driver)
        order_tape_page.open_page(data.Urls.ORDER_TAPE)
        first_order = order_tape_page.find_order_number().text
        assert order_number == first_order

    @pytest.mark.parametrize("order_number_locator, test_name", [
        (FeedPageLocators.ALL_ORDER_NUMBER, 'Выполнено за всё время увеличивается'),
        (FeedPageLocators.TODAY_ORDER_NUMBER, 'Выполнено за сегодня увеличивается')
    ])
    @allure.description("Этот тест проверяет что при создании нового заказа счётчик {test_name}")
    def test_order_completion_counter_increases(self, driver, user_data, order_number_locator, test_name):
        # Открываем страницу личного кабинета
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(data.Urls.LOGIN_PAGE)

        # Логинимся
        email, password = user_data
        personal_account_page.input_email(email)
        personal_account_page.input_password(password)
        personal_account_page.click_login_button()
        time.sleep(2)

        # Переходим в историю заказов и получаем текущее значение счётчика выполненных заказов
        order_tape_page = OrderTapePage(driver)
        order_tape_page.open_page(data.Urls.ORDER_TAPE)
        completed_orders_count_before = int(order_tape_page.wait_and_find_element(order_number_locator).text)

        # Создаём новый заказ
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.STELLAR_BURGERS)
        bun_element = main_page.find_ingredient_bun()
        drop_area = main_page.find_space_to_add_ingredient()
        actions = ActionChains(driver)
        actions.drag_and_drop(bun_element, drop_area).perform()
        time.sleep(2)
        main_page.click_button_create_order()
        time.sleep(5)

        order_tape_page.open_page(data.Urls.ORDER_TAPE)
        completed_orders_count_after = int(personal_account_page.wait_and_find_element(order_number_locator).text)
        assert completed_orders_count_after > completed_orders_count_before

    @allure.description("Этот тест проверяет что после оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress_section(self, driver, user_data):
        # Открываем страницу личного кабинета
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(data.Urls.LOGIN_PAGE)
        # Логинимся
        email, password = user_data
        personal_account_page.input_email(email)
        personal_account_page.input_password(password)
        personal_account_page.click_login_button()
        time.sleep(2)

        # Создаём новый заказ
        main_page = MainPage(driver)
        main_page.find_collect_burger()
        bun_element = main_page.find_ingredient_bun()
        drop_area = main_page.find_space_to_add_ingredient()
        actions = ActionChains(driver)
        actions.drag_and_drop(bun_element, drop_area).perform()
        time.sleep(2)
        main_page.click_button_create_order()
        time.sleep(5)
        order_number = "0" + str(main_page.find_order_number().text)

        order_tape_page = OrderTapePage(driver)
        order_tape_page.open_page(data.Urls.ORDER_TAPE)
        time.sleep(5)
        order_to_work = order_tape_page.find_order_to_work().text
        assert order_number == order_to_work

