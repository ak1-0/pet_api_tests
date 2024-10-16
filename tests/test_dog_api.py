import requests

DOG_API_URL = "https://dog.ceo/api"

def test_random_dog_image():
    response = requests.get(f"{DOG_API_URL}/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["message"], str)  # URL изображения

def test_list_breeds():
    response = requests.get(f"{DOG_API_URL}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["message"], dict)  # Список пород