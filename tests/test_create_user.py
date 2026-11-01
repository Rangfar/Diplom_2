import allure

@allure.suite("Проверка создания пользователя")
class TestCreateUser:
    @allure.title("Создание уникального пользователя с валидными данными")
    def test_create_unique_user(self, user):
        user.create_random_register_full_data()
        user.send_request_create_user()
        assert user.create_response.json()["success"] == True

    @allure.title("Регистрация уже зарегистрированного пользователя")
    def test_create_user_already_registred(self, user):
        user.create_random_register_full_data()
        user.send_request_create_user()
        user.send_request_create_user()
        assert user.create_response.status_code == 403
        assert user.create_response.json()["success"] == False
        assert user.create_response.json()["message"] == "User already exists"

    @allure.title("Регистрация пользователя без указания email")
    def test_create_user_without_email(self, user):
        user.create_random_register_data_without_email()
        user.send_request_create_user()
        assert user.create_response.status_code == 403
        assert user.create_response.json()["success"] == False
        assert user.create_response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Регистрация пользователя без указания пароля")
    def test_create_user_without_password(self, user):
        user.create_random_register_data_without_password()
        user.send_request_create_user()
        assert user.create_response.status_code == 403
        assert user.create_response.json()["success"] == False
        assert user.create_response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Регистрация пользователя без указания имени")
    def test_create_user_witout_name(self, user):
        user.create_random_register_data_without_name()
        user.send_request_create_user()
        assert user.create_response.status_code == 403
        assert user.create_response.json()["success"] == False
        assert user.create_response.json()["message"] == "Email, password and name are required fields"