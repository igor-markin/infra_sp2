# API YamDB

## Описание
Проект YaMDb собирает отзывы пользователей на произведения.

## Как запустить приложение?
`docker-compose up -d --build`

## Как создать суперпользователя?
`docker exec -ti <container> bash`
`python manage.py createsuperuser`

## Как заполнить базу тестовыми данными?
`docker exec -ti <container> bash`
`python manage.py loaddata fixtures.json`