import requests
import allure
from data import Urls

class ApiRequests:
    def __init__(self):
        self.base_url = Urls.API_STELLAR_BURGERS

    @allure.step("Отправка POST-запроса на эндпоинт: {endpoint}")
    def post(self, endpoint, headers=None, json=None):
        url = f'{self.base_url}{endpoint}'
        return requests.post(url, headers=headers, json=json)
