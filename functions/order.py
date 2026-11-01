import allure
import requests
from constants import Constants

class Order:
    @allure.step("Отправка запроса на создание заказа с авторизацией")
    def create_order_with_login(self, token, payload):
        headers = {
            'Authorization': token
        }
        self.create_order_response = requests.post(Constants.ORDER_CREATE_URL, headers=headers, data = payload)

    @allure.step("Отправка запроса на создание заказа без авторизации")
    def create_order_without_login(self, payload):
        self.create_order_response = requests.post(Constants.ORDER_CREATE_URL, data = payload)