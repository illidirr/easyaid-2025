FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# ИСПРАВЛЕННАЯ СТРОКА - используйте переменную PORT
CMD python manage.py migrate && gunicorn EasyAid.wsgi --bind 0.0.0.0:$PORT