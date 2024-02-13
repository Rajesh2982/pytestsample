import pytest
import requests

@pytest.mark.parametrize("user_id", [1, 2, 12])  # Example parameterized test
def test_get_user(user_id):
     response = requests.get("https://jsonplaceholder.typicode.com/users/{user_id}")
     assert response.status_code == 200
     print(response)
     assert response.json()["id"] == user_id

def test_create_user():
    new_user = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=new_user)
    assert response.status_code == 201
    assert response.json()["id"] is not None
    # You can add more assertions based on the response data

