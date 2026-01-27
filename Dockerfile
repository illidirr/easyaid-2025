FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# Ключевая строка - команда запуска
CMD gunicorn EasyAid.wsgi:application --bind 0.0.0.0:$PORT