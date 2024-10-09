from selenium.webdriver.common.by import By

class MainPageLocators:
    COLLECT_BURGER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_TAPE_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    ADD_INGREDIENT = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")
    INGREDIENT_INFO = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/div/div/h2[text()='Детали ингредиента']")
    CLOSE_INGREDIENT_INFO_BUTTON = (By.XPATH, "(//button[contains(@class, 'Modal_modal__close__TnseK')])[1]")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    COUNTER_BUN = (By.XPATH, "//*[contains(@class, 'counter_counter__num')][1]")
    ORDER_NUMBER = (By.XPATH, "(//section[contains(@class, 'Modal_modal_opened')]/div/div/h2)")