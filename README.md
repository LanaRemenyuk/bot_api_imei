# IMEI checker bot

Программа для проверки IMEI устройств (API Flask + TG Bot)
---

## Инструкции по запуску

1. Склонируйте репозиторий:
   ```bash
   git clone git@github.com:LanaRemenyuk/bot_api_imei.git
   cd bot_api_imei
  

2. Создайте `.env` файл в корне проекта (шаблон будет направлен с решением).

3. Запустите проект:

```bash

docker-compose up --build
```

- Локальный сервер будет доступен по адресу: [http://localhost:5000](http://localhost:5000).
- Тестовый юзер загружается в docker-compose, для этого нужно внести свои данные в env.

## Эндпоинты

1. */api/check-imei*: 
Параметры запроса:
imei (строка, обязательный) — IMEI устройства.
token (строка, обязательный) — токен авторизации.

Ответ:
JSON с информацией о IMEI.

## Автор: 
- LanaRemenyuk