import requests

DUCK_API_URL = "https://random-d.uk/api/random"

def test_duck_image_response_structure():
    response = requests.get(DUCK_API_URL)
    assert response.status_code == 200
    data = response.json()
    # Проверка структуры ответа
    assert isinstance(data, dict)
    assert "url" in data
    assert "status" in data
    assert data["status"] == "success"  # Предполагается, что API возвращает статус

def test_duck_image_multiple_requests():
    # Проверка, что разные запросы возвращают разные изображения
    urls = set()
    for _ in range(10):
        response = requests.get(DUCK_API_URL)
        assert response.status_code == 200
        data = response.json()
        urls.add(data["url"])
    assert len(urls) > 1  # Убедитесь, что получены разные URL

def test_invalid_format_request():
    # Проверка обработки некорректного формата
    response = requests.get(f"{DUCK_API_URL}?format=png")  # Формат не поддерживается
    assert response.status_code == 400  # Предполагается, что API возвращает 400 для некорректного формата

def test_duck_image_content_type():
    response = requests.get(DUCK_API_URL)
    assert response.status_code == 200
    content_type = response.headers["Content-Type"]
    assert content_type == "application/json"  # Проверка типа контента

def test_duck_image_url_validity():
    response = requests.get(DUCK_API_URL)
    assert response.status_code == 200
    data = response.json()
    url = data["url"]
    # Проверка, что URL доступен и возвращает изображение
    image_response = requests.get(url)
    assert image_response.status_code == 200
    assert "image" in image_response.headers["Content-Type"]  # Проверка, что контент - это изображение
