mport requests

FOX_API_URL = "https://randomfox.ca/floof/"

def test_random_fox_image():
    response = requests.get(FOX_API_URL)
    assert response.status_code == 200
    data = response.json()
    assert "image" in data
    assert isinstance(data["image"], str)  # URL изображения

def test_fox_image_response_structure():
    response = requests.get(FOX_API_URL)
    assert response.status_code == 200
    data = response.json()
    # Проверка структуры ответа
    assert isinstance(data, dict)
    assert "image" in data
    assert "link" in data  # Если API возвращает ссылку на источник
    assert data["link"] is not None  # Проверка, что ссылка не пустая

def test_multiple_fox_requests():
    # Проверка, что разные запросы возвращают разные изображения
    urls = set()
    for _ in range(10):
        response = requests.get(FOX_API_URL)
        assert response.status_code == 200
        data = response.json()
        urls.add(data["image"])
    assert len(urls) > 1  # Убедиться, что получены разные URL

def test_fox_image_content_type():
    response = requests.get(FOX_API_URL)
    assert response.status_code == 200
    content_type = response.headers["Content-Type"]
    assert content_type == "application/json"  # Проверка типа контента

def test_fox_image_url_validity():
    response = requests.get(FOX_API_URL)
    assert response.status_code == 200
    data = response.json()
    url = data["image"]
    # Проверка, что URL доступен и возвращает изображение
    image_response = requests.get(url)
    assert image_response.status_code == 200
    assert "image" in image_response.headers["Content-Type"]  # Проверка, что контент - это изображение

def test_fox_api_rate_limit():
    # Проверка ограничения по частоте запросов (если применимо)
    for _ in range(10):
        response = requests.get(FOX_API_URL)
        assert response.status_code == 200
    # Это просто проверка на 10 успешных запросов.
