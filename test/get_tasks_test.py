import allure
import requests
from config import BASE_URL


@allure.title("Получение списка задач")
@allure.story("CRUD: Read")
@allure.severity(allure.severity_level.BLOCKER)
def test_get_tasks():
    with allure.step("Отправить GET-запрос"):
        response = requests.get(BASE_URL)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что вернулся список"):
        assert isinstance(response.json(), list)
