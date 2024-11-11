import requests
import pytest

URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def user_data():
    return {
        "id": 0,
        "username": "trust",
        "firstName": "Trust",
        "lastName": "Me",
        "email": "mail@example.com",
        "password": "123123",
        "phone": "1234567890",
        "userStatus": 0
    }

@pytest.fixture
def user_data_list():
    return [{
        "id": 1,
        "username": "trust",
        "firstName": "Trust",
        "lastName": "Me",
        "email": "mail@example.com",
        "password": "123123",
        "phone": "1234567890",
        "userStatus": 0
    },
        {
            "id": 2,
        "username": "trust2",
        "firstName": "Don't Trust",
        "lastName": "Me",
        "email": "mail2@example.com",
        "password": "123123",
        "phone": "987654321",
        "userStatus": 1
        }]

@pytest.fixture
def store_order():
    return {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2024-11-11T16:55:59.437Z",
        "status": "placed",
        "complete": True
    }


def test_user_create(user_data_list):
    response = requests.post(f"{URL}/user/createWithArray", json=user_data_list, headers=HEADERS)
    assert response.status_code == 200, f"Код ответа POST-запроса на создание: {response.status_code}"

def test_user_login(user_data):
    response = requests.get(f"{URL}/user/login", data={'username': user_data['username'], 'password': user_data['password']}, headers=HEADERS)
    assert response.status_code == 200, f"Код ответа GET-запроса на логин: {response.status_code}"

def test_user_update(user_data):
    updated = user_data.copy()
    updated['username'] = "trustUpdated"
    response = requests.put(f"{URL}/user/trust", json=updated, headers=HEADERS)
    assert response.status_code == 200, f"Код ответа PUT-запроса на обновление: {response.status_code}"

def test_user_get(user_data):
    response = requests.get(f"{URL}/user/{user_data['username']}", json={'username': user_data['username']}, headers=HEADERS)
    assert response.status_code == 200, f"Код ответа GET-запроса на получение: {response.status_code}"

def test_store_pet_inventory():
    response = requests.get(f"{URL}/store/inventory", headers=HEADERS)
    assert response.status_code == 200, f"Код ответа GET-запроса на инвентарь: {response.status_code}"

def test_store_order(store_order):
    response = requests.post(f"{URL}/store/order", json=store_order, headers=HEADERS)
    assert response.status_code == 200, f"Кот ответа POST-запроса на размещение заказа: {response.status_code}"
    store_data = response.json()
    assert store_data['id'] == store_order['id']

def test_store_get_order(store_order):
    response = requests.get(f"{URL}/store/order/{store_order['id']}", headers=HEADERS)
    assert response.status_code == 200
    store_data = response.json()
    assert store_data['id'] == store_order['id']

def test_store_delete_order(store_order):
    response = requests.delete(f"{URL}/store/order/{store_order['id']}", headers=HEADERS)
    assert response.status_code == 200
    response = requests.get(f"{URL}/store/order/{store_order['id']}", headers=HEADERS)
    assert response.status_code == 404
