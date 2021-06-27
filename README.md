# API YamDB

## Описание
Проект YaMDb собирает отзывы пользователей на произведения.

## Основные технологии
`Django Rest`, `PostgeSQL`, `Nginx`, `Docker-composer`

## Переменные окружения
Переменные хранятся в файле `/api_yamdb/.env.dev`.
Его нужно переименовать в `.dev` и подставить необходимые значения.

`DEBUG` — Режим разработки (True/False).

`SECRET_KEY` — секретный ключ для создания хешей.

`DATABASE_URL` — URL для подключения к базе данных.

## Настройки проекта
Глобальные настройки хранятся в файле `api_yamdb/settings.py`.

**Настройки, которые можно сразу поменять**

`ALLOWED_HOSTS` — домены и ip-адреса, на которых разрешено работать проекту.

`TIME_ZONE` — ваш часовой пояс.

`SEND_MAIL_EMAIL` — почта администратора.

## Как запустить проект?
Перейдите в папку проекта и выполните команду:

```bash
docker-compose up -d --build
```

После запуска — API будет доступен по адресу `/api/v1/`.

## Документация
Документация будет доступна после запуска проекта по адресу `/redoc/`.

## Как создать суперпользователя?
```bash
docker-compose exec -ti container_name python manage.py createsuperuser
```

## Как заполнить базу тестовыми данными?
```bash
docker-compose exec -ti container_name python manage.py loaddata fixtures.json
```

## Если остались вопросы
Не стесняйтесь, пишите мне на почту:
[9588604@gmail.com](mailto:9588604@gmail.com "9588604@gmail.com").
