FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# Исправьте эту строку:
CMD ["gunicorn", "gEasyAid.wsgi:application", ""--bind", "0.0.0.0:8080"]"]