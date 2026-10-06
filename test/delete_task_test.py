import allure
import requests
from faker import Faker

from config import BASE_URL

fake = Faker()


@allure.title("Удаление задачи")
@allure.story("CRUD: Delete")
def test_delete():
    with allure.step("Создать задачу"):
        body = {"title": fake.sentence(), "completed": False}
        response = requests.post(BASE_URL, json=body)
        task_id = response.json()["id"]

    with allure.step("Удалить задачу"):
        response = requests.delete(f"{BASE_URL}{task_id}")

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200
