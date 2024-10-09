import allure

from pages.base_page import BasePage
from locators.feed_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Нажимаем на кнопку Конструктор')
    def click_constructor_button(self):
         self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажимаем на кнопку Лента заказов')
    def click_order_tape_button(self):
        self.wait_and_find_element(MainPageLocators.ORDER_TAPE_BUTTON)
        self.click_element(MainPageLocators.ORDER_TAPE_BUTTON)

    @allure.step('Нажимаем на ингредиент')
    def click_ingredient_bun(self):
        self.wait_and_find_element(MainPageLocators.BUN)
        self.click_element(MainPageLocators.BUN)

    @allure.step('Находим ингредиент')
    def find_ingredient_bun(self):
        return self.wait_and_find_element(MainPageLocators.BUN)

    @allure.step('Находим место добавления ингредиента')
    def find_space_to_add_ingredient(self):
        return self.wait_and_find_element(MainPageLocators.ADD_INGREDIENT)

    @allure.step('Находим каунтер ингредиента')
    def find_counter_bun(self):
        return self.wait_and_find_element(MainPageLocators.COUNTER_BUN)

    @allure.step('Нажимаем на кнопку закрыть Детали ингредиента')
    def click_ingredient_info_close(self):
         self.click_element(MainPageLocators.CLOSE_INGREDIENT_INFO_BUTTON)

    @allure.step('Нажимаем на кнопку  Оформить заказ')
    def click_button_create_order(self):
        self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Находим заголовок Детали ингредиента')
    def find_ingredient_info(self):
        return self.wait_and_find_element(MainPageLocators.INGREDIENT_INFO)

    @allure.step('Находим заголовок Соберите бургер')
    def find_collect_burger(self):
        return self.wait_and_find_element(MainPageLocators.COLLECT_BURGER)

    @allure.step('Находим заголовок Лента заказов')
    def find_order_tape(self):
        return self.wait_and_find_element(FeedPageLocators.ORDER_TAPE)

    @allure.step('Детали ингредиента исчез после закрытия')
    def check_ingredient_info_disappear(self):
        return self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_INFO)

    @allure.step('Находим кнопку Оформить заказ')
    def find_button_create_order(self):
        return self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Находим номер заказа')
    def find_order_number(self):
        return self.wait_and_find_element(MainPageLocators.ORDER_NUMBER)

