import requests, pytest
from data.helpers import register_new_courier_and_return_login_password
from data.urls import URL_COURIER


@pytest.fixture
def courier():
    data = register_new_courier_and_return_login_password()
    yield data

    login_response = requests.post(
        URL_COURIER + '/login',
        json={
            "login": data["login"],
            "password": data["password"]
        }
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]

        requests.delete(f"{URL_COURIER}/{courier_id}")
