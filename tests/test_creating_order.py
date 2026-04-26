import requests, pytest, allure
from data.urls import URL_ORDER
from data.base_order import BASE_ORDER


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

        payload = BASE_ORDER.copy()
        payload["color"] = color

        response = requests.post(
            URL_ORDER,
            json=payload
        )

        assert response.status_code == 201
        assert "track" in response.json()

        cancel_order.append(response.json()["track"])
