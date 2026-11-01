import allure
from data import ingredients

@allure.suite("Проверка создания заказов")
class TestCreateOrder:
    @allure.title("Проверка создания заказа с авторизацией со списком корректных ингредиентов")
    def test_create_order_with_login_and_correct_ingredients(self, user, order):
        user.create_random_register_full_data()
        user.send_request_create_user()
        payload = ingredients
        order.create_order_with_login(user.token, payload)
        assert "name" in order.create_order_response.json()
        assert len(order.create_order_response.json()["name"]) > 1
        assert "order" in order.create_order_response.json()
        assert "number" in order.create_order_response.json()["order"]
        assert order.create_order_response.json()["success"] == True

    @allure.title("Проверка создания заказа без авторизации со списком корректных ингредиентов")
    def test_create_order_without_login_and_correct_ingredients(self, order):
        payload = ingredients
        order.create_order_without_login(payload)
        assert "name" in order.create_order_response.json()
        assert len(order.create_order_response.json()["name"]) > 1
        assert "order" in order.create_order_response.json()
        assert "number" in order.create_order_response.json()["order"]
        assert order.create_order_response.json()["success"] == True

    @allure.title("Проверка создания заказа с авторизацией без ингредиентов")
    def test_create_order_with_login_and_without_ingredietns(self, user, order):
        user.create_random_register_full_data()
        user.send_request_create_user()
        payload = {"ingredients": [""]}
        order.create_order_with_login(user.token, payload)
        assert order.create_order_response.status_code == 400
        assert order.create_order_response.json()["success"] == False
        assert order.create_order_response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Проверка создания заказа без авторизации и без ингредиентов")
    def test_create_order_without_login_and_without_ingredients(self, order):
        payload = {"ingredients": [""]}
        order.create_order_without_login(payload)
        assert order.create_order_response.status_code == 400
        assert order.create_order_response.json()["success"] == False
        assert order.create_order_response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Проверка создания заказов с авторизацией и некорретным списком ингредиентов")
    def test_create_order_with_login_and_incorrect_ingredients(self, user, order):
        user.create_random_register_full_data()
        user.send_request_create_user()
        payload = {"ingredients": ["булочка из творога", "имбирный желудь"]}
        order.create_order_with_login(user.token, payload)
        assert order.create_order_response.status_code == 500

    @allure.title("Проверка создания заказов без авторизации и некорректным списком ингредиентов")
    def test_create_order_without_login_and_incorrect_ingredients(self, order):
        payload = {"ingredients": ["булочка из творога", "имбирный желудь"]}
        order.create_order_without_login(payload)
        assert order.create_order_response.status_code == 500
