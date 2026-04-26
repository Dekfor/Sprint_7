import requests, pytest
from data.helpers import register_new_courier_and_return_login_password
from data.urls import URL_COURIER, URL_ORDER


@pytest.fixture
def courier_data():
    login, password, first_name = register_new_courier_and_return_login_password()

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }

@pytest.fixture
def courier(courier_data):

    requests.post(URL_COURIER, data=courier_data)
    yield courier_data

    login_resp = requests.post(URL_COURIER + "/login", data={
        "login": courier_data["login"],
        "password": courier_data["password"]
    })

    if login_resp.status_code == 200:
        courier_id = login_resp.json()["id"]
        requests.delete(f"{URL_COURIER}/{courier_id}")

@pytest.fixture
def cancel_order():
    tracks = []

    yield tracks

    for track in tracks:
        requests.put(
            f"{URL_ORDER}/cancel",
            json={"track": track}
        )
