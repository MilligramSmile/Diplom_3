import allure

from locators.feed_locators import FeedPageLocators
from locators.orders_tape_locators import OrderTapePageLocators
from pages.base_page import BasePage


class OrderTapePage(BasePage):

    @allure.step('Нажимаем на заказ')
    def click_order_item(self):
        self.wait_and_find_element(OrderTapePageLocators.ORDER_ITEM)
        self.click_element(OrderTapePageLocators.ORDER_ITEM)

    @allure.step('Находим окно с деталями')
    def find_order_info(self):
        return self.wait_and_find_element(OrderTapePageLocators.ORDER_MODAL)

    @allure.step('Находим заказ в работе')
    def find_order_to_work(self):
        return self.wait_and_find_element(FeedPageLocators.ORDER_TO_WORK)

    @allure.step('Находим номер заказа в списке')
    def find_order_number(self):
        return self.wait_and_find_element(FeedPageLocators.FIRST_ORDER_NUMBER)