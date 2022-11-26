# Backend-сервис для организации фотогалерии пользователей

## Общее описание

1. Воспользоваться сервисом могут только зарегистрированные пользователи.
2. Регистрация, авторизация:
    - Регистрация пользователя: POST - http://localhost:8000/auth/users/ (username, имя, фамилия)
    - Получение токена: POST - http://localhost:8000/auth/token/login/ (username, пароль)
3. API:
    - Добавить фото: POST - http://localhost:8000/api/v1/gallery (token, file)
    - Удалить(только владелец), получить фото: DELETE, GET - http://localhost:8000/api/v1/gallery/<id>
    - Получить список фото: GET - http://localhost:8000/api/v1/gallery
    - Получить текущего пользователя: GET - http://localhost:8000/api/v1/currient
    - Удалить всю галерею (только для администратора): DELETE - http://localhost:8000/api/v1/destroy

## Установка проекта на локальный компьютер:

1. Должен быть предустановлен менеджер зависимостей `poetry`. Или установите `poetry` любым удобным способом. 
   Например: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -` 
2. Выполните клонирование репозитория: `https://github.com/suband74/DFA`
3. Затем выполните установку зависимостей проекта: `poetry install`
4. Установить docker и docker-compose. Инструкции по установке доступны в официальной документации.
5. В папке с проектом выполнить команду:
```
docker-compose up
```
