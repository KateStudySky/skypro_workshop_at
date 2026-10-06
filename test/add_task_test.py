import allure
import requests
from faker import Faker

from config import BASE_URL

fake = Faker()


@allure.title("Создание задачи")
@allure.story("CRUD: Create")
@allure.severity(allure.severity_level.CRITICAL)
def test_add():
    title = fake.sentence()
    body = {"title": title, "completed": False}

    with allure.step("Отправить POST-запрос на создание задачи"):
        response = requests.post(BASE_URL, json=body)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что в ответе вернулся переданный title"):
        assert response.json()["title"] == title

    with allure.step("Проверить, что у задачи есть id"):
        assert response.json()["id"] is not None
