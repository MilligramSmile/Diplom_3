import pytest
import time
from selenium import webdriver

from api_requests import ApiRequests
from data import Urls
from utils import generate_user_data


@pytest.fixture(scope='function')
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    yield chrome
    chrome.quit()


# def driver():
#     firefox = webdriver.Firefox()
#     firefox.maximize_window()
#     yield firefox
#     firefox.quit()

@pytest.fixture
def user_data():
    api_requests = ApiRequests()
    email, password, name = generate_user_data()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = api_requests.post(Urls.API_USER_REGISTER, json=payload)
    # Проверим успешную регистрацию
    assert response.status_code == 200
    # Вернем данные пользователя для использования в тестах
    time.sleep(5)
    return email, password

