import allure
import requests
from config import BASE_URL


@allure.title("Создание задачи с эмоджи названием")
@allure.story("CRUD: Create")
@allure.severity(allure.severity_level.NORMAL)
def test_add():

    body = {"title": "Test 🚀", "completed": False}

    with allure.step("Отправить POST-запрос на создание задачи"):
        response = requests.post(BASE_URL, json=body)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что в ответе вернулся переданный title"):
        assert response.json()["title"] == "Test 🚀"

    with allure.step("Проверить, что у задачи есть id"):
        assert response.json()["id"] is not None
