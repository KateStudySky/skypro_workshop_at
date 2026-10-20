import allure
import requests
from faker import Faker
from config import BASE_URL


fake = Faker()


@allure.title("Отметка задачи выполненной")
@allure.story("CRUD: Update")
@allure.severity(allure.severity_level.NORMAL)
def test_edit():
    with allure.step("Создать задачу"):
        body = {"title": fake.sentence(), "completed": False}
        response = requests.post(BASE_URL, json=body)
        task_id = response.json()["id"]

    with allure.step("Отметить задачу выполненной"):
        body = {"completed": True}
        response = requests.patch(f"{BASE_URL}{task_id}", json=body)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Получить задачу и проверить новый title"):
        response = requests.get(f"{BASE_URL}{task_id}")
        assert response.status_code == 200
        assert response.json()["completed"] == True
