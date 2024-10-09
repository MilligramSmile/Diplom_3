from selenium.webdriver.common.by import By

class OrderTapePageLocators:
    ORDER_MODAL = (By.XPATH, "(//section[contains(@class, 'Modal_modal_opened')])")
    ORDER_ITEM = (By.XPATH, "(//ul[contains(@class,'OrderFeed_list')]//li[1])")