import requests, allure, pytest
from data.urls import URL_COURIER


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание")
    def test_create_courier_success(self, courier):
        payload = {
        "login": courier[0],
        "password": courier[1],
        "firstName": courier[2]
        }

        response = requests.post(
            URL_COURIER,
            data=payload
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Создание двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self):
        payload = {
            "login": "ninja123",
            "password": "1234",
            "firstName": "saske"
        }

        requests.post(
            URL_COURIER,
            data=payload
        )

        response = requests.post(
            URL_COURIER,
            data=payload
        )

        assert response.status_code == 409
        assert response.json()["message"] == \
            "Этот логин уже используется"

    @allure.title("Создание без заполнения обязательного поля")

    @pytest.mark.parametrize("payload", [
        {"login": "nopassword123", "firstName": "saske"}, 
        {"password": "1234", "firstName": "saske"},       
    ])
    
    def test_create_without_required_field_returns_error(self, payload):

        response = requests.post(
            URL_COURIER,
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == \
            "Недостаточно данных для создания учетной записи"
