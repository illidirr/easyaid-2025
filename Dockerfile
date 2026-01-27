FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# Фиксированный порт 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]