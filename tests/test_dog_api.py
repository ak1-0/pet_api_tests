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

def test_breed_images():
    breed = "retriever/golden"
    response = requests.get(f"{DOG_API_URL}/breed/{breed}/images")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["message"], list)  # Список URL изображений

def test_random_breed_image():
    breed = "hound/afghan"
    response = requests.get(f"{DOG_API_URL}/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["message"], str)  # URL изображения

def test_random_sub_breed_image():
    breed = "hound"
    sub_breed = "afghan"
    response = requests.get(f"{DOG_API_URL}/breed/{breed}/{sub_breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["message"], str)  # URL изображения

def test_non_existent_breed():
    breed = "unicorn"
    response = requests.get(f"{DOG_API_URL}/breed/{breed}/images")
    assert response.status_code == 404

def test_breed_image_count():
    # Проверка количества изображений породы
    breed = "retriever/golden"
    response = requests.get(f"{DOG_API_URL}/breed/{breed}/images")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert len(data["message"]) > 0
    assert isinstance(data["message"], list)

def test_sub_breed_list():
    # Получение списка подвидов породы
    breed = "hound"
    response = requests.get(f"{DOG_API_URL}/breed/{breed}/list")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
