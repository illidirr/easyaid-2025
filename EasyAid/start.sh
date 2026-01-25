#!/bin/bash
# Установка зависимостей
pip install -r requirements.txt

# Сборка статики (если нужно)
python manage.py collectstatic --noinput

# Запуск приложения
gunicorn EasyAid.wsgi:application --bind 0.0.0.0:$PORT
{
  "build": "pip install -r requirements.txt && python manage.py collectstatic --noinput",
  "start": "gunicorn EasyAid.EasyAid.wsgi:application --bind 0.0.0.0:$PORT"
}