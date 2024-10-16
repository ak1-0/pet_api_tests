import requests

CAT_API_URL = "https://api.thecatapi.com/v1"

def test_random_cat_image():
    response = requests.get(f"{CAT_API_URL}/images/search")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "url" in data[0]  # URL изображения

def test_list_breeds():
    response = requests.get(f"{CAT_API_URL}/breeds")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Список пород