# Pet API Tests
[![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-blue.svg)](https://docs.pytest.org/)
[![Requests](https://img.shields.io/badge/Requests-2.26.0-brightgreen.svg)](https://docs.python-requests.org/en/latest/)
![Work In Progress](https://img.shields.io/badge/Work%20In%20Progress-orange?style=flat-square)

## Описание проекта
**Pet API Tests** - это проект, который включает автоматические тесты для проверки работоспособности публичных API для котов и собак. Проект использует библиотеки `Pytest` и `Requests` для выполнения тестов и проверки корректности работы API.

## Файлы проекта
- **test_cat_api.py**: Содержит тесты для [The Cat API](https://thecatapi.com/).
- **test_dog_api.py**: Содержит тесты для [Dog CEO API](https://dog.ceo/dog-api/).

## Установка и запуск тестов
1. **Клонируйте репозиторий на свой компьютер**:
    ```bash
    git clone https://github.com/ak1-0/pet_api_tests.git
    cd pet_api_tests
    ```

2. **Создайте виртуальное окружение и активируйте его**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Запустите тесты**:
    ```bash
    pytest
    ```

## Описание тестов
### Тесты для The Cat API (test_cat_api.py)
- **test_random_cat_image**: Проверяет получение случайного изображения кота.
- **test_list_breeds**: Проверяет получение списка всех пород котов.

### Тесты для Dog CEO API (test_dog_api.py)
- **test_random_dog_image**: Проверяет получение случайного изображения собаки.
- **test_list_breeds**: Проверяет получение списка всех пород собак.
- **test_breed_images**: Проверяет получение изображений для заданной породы собак.
- **test_random_breed_image**: Проверяет получение случайного изображения заданной породы собак.
- **test_random_sub_breed_image**: Проверяет получение случайного изображения под-породы собак.
- **test_non_existent_breed**: Проверяет обработку запроса для несуществующей породы.

## Вклад
Не стесняйтесь открывать вопросы и отправлять pull-запросы. Будь то исправление ошибки, новая функция или предложение по улучшению, вклады всегда приветствуются!

## Лицензия
Этот проект лицензирован под лицензией MIT - см. файл LICENSE для подробностей.
