import requests, allure
from data.helpers import register_new_courier_and_return_login_password
from data.urls import URL_COURIER


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация")
    def test_login_success(self):
        courier = register_new_courier_and_return_login_password()

        payload = {
            "login": courier[0],
            "password": courier[1]
        }

        response = requests.post(
            URL_COURIER + '/login',
            data=payload
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация с неверным паролем")
    def test_login_wrong_password(self):
        courier = register_new_courier_and_return_login_password()

        payload = {
            "login": courier[0],
            "password": "wrong_password"
        }

        response = requests.post(
            URL_COURIER + '/login',
            data=payload
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация без поля логин")
    def test_login_without_login(self):
        payload = {
            "password": "1234"
        }

        response = requests.post(
            URL_COURIER + '/login',
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Авторизация несуществующей учетной записи")
    def test_login_nonexistent_user(self):
        payload = {
            "login": "somefakeuser12345",
            "password": "1234"
        }

        response = requests.post(
            URL_COURIER + '/login',
            data=payload
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
        