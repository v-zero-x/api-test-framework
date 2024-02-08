import requests

BASE_URL = "http://host.docker.internal:5001"

def test_get_items():
    response = requests.get(f"{BASE_URL}/items")
    assert response.status_code == 200
    assert isinstance(response.json().get('items'), list)

def test_create_item():
    new_item = {"name": "Test Item"}
    response = requests.post(f"{BASE_URL}/items", json=new_item)
    assert response.status_code == 201
    assert response.json().get('name') == new_item['name']

def test_update_item():
    update_data = {"name": "Updated Item"}
    response = requests.put(f"{BASE_URL}/items/1", json=update_data)
    assert response.status_code == 200
    assert response.json().get('name') == update_data['name']

def test_delete_item():
    response = requests.delete(f"{BASE_URL}/items/1")
    assert response.status_code == 200
