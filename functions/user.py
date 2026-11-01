import requests
import allure
from functions.base import generate_random_string, generate_random_number
from constants import Constants

class User:
    @allure.step("Генерация полного набора случайных данных")
    def create_random_register_full_data(self):
        self.email = f'{generate_random_string(8)}@toptop.com'
        self.password = generate_random_number(1000, 10000000)
        self.name = generate_random_string(7)
        self.payload = {
                    "email": self.email,
                    "password": self.password,
                    "name": self.name
                }

    @allure.step("Генерация случайных пароля и имени")
    def create_random_register_data_without_email(self):
        self.password = generate_random_number(1000, 10000000)
        self.name = generate_random_string(7)
        self.payload = {
            "password": self.password,
            "name": self.name
        }

    @allure.step("Генерация случайных email и имени")
    def create_random_register_data_without_password(self):
        self.email = f'{generate_random_string(8)}@toptop.com'
        self.name = generate_random_string(7)
        self.payload = {
                "email": self.email,
                "name": self.name
        }

    @allure.step("Генерация случайных email и пароля")
    def create_random_register_data_without_name(self):
        self.email = f'{generate_random_string(8)}@toptop.com'
        self.password = generate_random_number(1000, 10000000)
        self.payload = {
                "email": self.email,
                "password": self.password
        }

    @allure.step("Отправка запроса на создание пользователя")
    def send_request_create_user(self):
        self.create_response = requests.post(Constants.USER_REGISTRATION_URL, data = self.payload)
        if self.create_response.status_code == 200:
            self.token = self.create_response.json()["accessToken"]
            
    @allure.step("Отправка запроса на удаление пользователя")
    def delete_user(self):
        headers = {
            'Authorization': self.token
        }
        self.delete_response = requests.delete(Constants.USER_DELETE_URL, headers=headers)

    @allure.step("Отправка запроса на вход в профиль пользователя")
    def login_user(self):
        payload = {
            "email": self.email,
            "password": self.password
        }
        self.login_response = requests.post(Constants.USER_LOGIN_URL, data = payload)