import requests, pytest, allure
from data.urls import URL_ORDER


@allure.feature("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])

    @allure.title("Проверка различных вариантов цвета самоката")
    def test_create_order_with_different_colors(self, color, cancel_order):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2026-04-25",
            "comment": "Saske, come back to Konoha",
            "color": color
        }

        response = requests.post(
            URL_ORDER,
            json=payload
        )

        assert response.status_code == 201
        assert "track" in response.json()

        cancel_order.append(response.json()["track"])
