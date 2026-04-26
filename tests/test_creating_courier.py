import requests, allure, pytest
from data.urls import URL_COURIER
from data.response_messages import COURIER_CREATE_ERROR, COURIER_DUPLICATE


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьер создаётся успешно")
    def test_create_courier_success(self, courier_data):

        response = requests.post(
            URL_COURIER,
            data=courier_data
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
        assert response.json()["message"] == COURIER_DUPLICATE

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
        assert response.json()["message"] == COURIER_CREATE_ERROR 
