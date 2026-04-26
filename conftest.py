import requests, pytest
from data.helpers import register_new_courier_and_return_login_password
from data.urls import URL_COURIER, URL_ORDER


@pytest.fixture
def courier():
    data = register_new_courier_and_return_login_password()
    yield data

    login_response = requests.post(URL_COURIER + "/login", data={
        "login": data[0],
        "password": data[1]
    })

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
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
