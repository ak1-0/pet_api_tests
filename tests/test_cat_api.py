import requests

CAT_API_URL = "https://api.thecatapi.com/v1"

def test_random_cat_image():
    response = requests.get(f"{CAT_API_URL}/images/search")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "url" in data[0] 

def test_list_breeds():
    response = requests.get(f"{CAT_API_URL}/breeds")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_breeds_search():
    # Поиск породы по имени
    breed_name = "beng"
    response = requests.get(f"{CAT_API_URL}/breeds/search?q={breed_name}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["name"].lower() == "bengal"

def test_random_cat_image_by_breed():
    # Получение случайного изображения конкретной породы
    breed_id = "beng"
    response = requests.get(f"{CAT_API_URL}/images/search?breed_id={breed_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "url" in data[0]

def test_categories_list():
    # Проверка категорий изображений
    response = requests.get(f"{CAT_API_URL}/categories")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]
