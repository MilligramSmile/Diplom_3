from selenium.webdriver.common.by import By

class LoginPageLocators:
    RECOVER_PASSWORD = (By.XPATH, "//p[contains(text(), 'Забыли пароль?')]//a[text()='Восстановить пароль']")
    INPUT_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    BUTTON_SAVED = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    BUTTON_RECOVER = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    HOVER_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    PASSWORD_INPUT_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
