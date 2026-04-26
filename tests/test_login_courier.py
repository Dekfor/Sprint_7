import requests, allure
from data.urls import URL_COURIER
from data.response_messages import COURIER_LOGIN_ERROR, COURIER_NOT_FOUND


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация")
    def test_login_success(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }

        response = requests.post(
            URL_COURIER + '/login',
            data=payload
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация с неверным паролем")
    def test_login_wrong_password(self, courier):

        payload = {
            "login": courier["login"],
            "password": "wrong_password"
        }

        response = requests.post(
            URL_COURIER + '/login',
            data=payload
        )

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND

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
        assert response.json()["message"] == COURIER_LOGIN_ERROR

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
        assert response.json()["message"] == COURIER_NOT_FOUND
     