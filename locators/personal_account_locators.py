from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, 'Пароль')
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY_ITEM_NUMBER = (By.XPATH, "(//div[contains(@class,'OrderHistory_textBox')]/p)")