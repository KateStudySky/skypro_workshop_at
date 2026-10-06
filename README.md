# Проект для воркшопа по автоматизации тестирования

Это общий репозиторий автотестов, над которым мы работаем командой.

## Что уже настроено

- Автотесты на `pytest` в папке `test/`
- CI на **GitHub Actions**: тесты запускаются автоматически при `push` и `pull request`
- **Allure-отчёт** сохраняется как артефакт в каждом запуске
- Защита ветки `main`: влить изменения можно только через `pull request` и только с зелёными тестами

## Что делаем на воркшопе

- Получаем доступ к репозиторию
- Клонируем репозиторий
- Создаём свою ветку
- Пишем один автотест
- Пушим ветку
- Смотрим результат в GitHub Actions
- Создаём pull request
- Проходим review и merge

## Шаги

- Склонировать репозиторий
- Установить зависимости: `pip install -r requirements.txt`
- Создать ветку `фамилия_ддмм`, например `ivanov_2305` и переключиться на нее: `git checkout -b ivanov_2305`
- Написать тест — один новый файл в папке `test/`, например `test/ivanov_completed_test.py`
- Запустить тесты: `pytest -s -v`
- Добавить файл в staging: `git add test/ivanov_completed_test.py`
- Сделать коммит: `git commit -m "Add test for task"`
- Запушить ветку: `git push -u origin ivanov_2305`
- Открыть вкладку **Actions** и дождаться прогона
- Создать pull request в `main` и приложить ссылку на прогон в Actions по своей ветке

## Правила

- Не трогать `.github/`, `pytest.ini`, `requirements.txt` и чужие тесты
- Один студент — один файл с тестом
- Красные PR не принимаются

## Полезные ссылки

- [Как создать pull request](https://docs.github.com/en/pull-requests)
- [Про GitHub Actions](https://docs.github.com/en/actions)
- [Allure pytest](https://docs.qameta.io/allure-report/frameworks/python/pytest/)