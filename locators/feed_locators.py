from selenium.webdriver.common.by import By

class FeedPageLocators:
    ORDER_TAPE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    ALL_ORDER_NUMBER = (By.XPATH, '//div[contains(@class, "undefined")]/p[contains(@class, "OrderFeed_number")]')
    TODAY_ORDER_NUMBER = (By.XPATH, '//div[2]/p[contains(@class, "OrderFeed_number")]')
    ORDER_TO_WORK = (By.XPATH, "(//ul[contains(@class,'OrderFeed_orderListReady')]//li[1])")
    FIRST_ORDER_NUMBER = (By.XPATH, '//div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, "text text_type_digits-default")][1]')

