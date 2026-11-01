import allure

@allure.suite("Проверка входа в профиль пользователя")
class TestLogin:
    @allure.title("Проверка входа в существующий профиль пользователя")
    def test_login_with_existing_user(self, user):
        user.create_random_register_full_data()
        user.send_request_create_user()
        user.login_user()
        assert user.login_response.json()["success"] == True
        assert "accessToken" in user.login_response.json()
        assert "refreshToken" in user.login_response.json()
        assert "user" in user.login_response.json()
        assert "email" in user.login_response.json()["user"]
        assert "name" in user.login_response.json()["user"]

    @allure.title("Проверка входа в профиль с неверным логином и паролем")
    def test_login_with_incorrect_login_and_password(self, user):
        user.create_random_register_full_data()
        user.login_user()
        assert user.login_response.status_code == 401
        assert user.login_response.json()["success"] == False
        assert user.login_response.json()["message"] == "email or password are incorrect"
