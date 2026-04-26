import requests, allure
from data.urls import URL_ORDER


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = requests.get(
            URL_ORDER
        )

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
        