FROM python:3.10

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Собираем статику
RUN python manage.py collectstatic --noinput

# Запускаем приложение
CMD ["gunicorn", "EasyAid.EasyAid.wsgi:application", "--bind", "0.0.0.0:$PORT"]