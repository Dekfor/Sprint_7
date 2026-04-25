import requests, random, allure
from data.urls import URL_COURIER


@allure.feature("Создание курьера")
class TestCreateCourier:

    def test_create_courier_success(self):
        payload = {
            "login": f"ninja{random.randint(10000,99999)}",
            "password": "1234",
            "firstName": "saske"
        }

        response = requests.post(
            URL_COURIER,
            data=payload
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

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

    def test_create_without_required_field_returns_error(self):
        payload = {
            "login": "nopassword123"
        }

        response = requests.post(
            URL_COURIER,
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == \
            "Недостаточно данных для создания учетной записи"

    def test_create_without_login_returns_error(self):
        payload = {
            "password": "1234",
            "firstName": "saske"
        }

        response = requests.post(
            URL_COURIER,
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == \
            "Недостаточно данных для создания учетной записи"
        
        