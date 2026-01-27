@'
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput

# ПРОВЕРОЧНЫЕ КОМАНДЫ ПЕРЕД ЗАПУСКОМ
RUN echo "=== Testing Django imports ==="
RUN python -c "import django; print(f'Django {django.__version__} OK')"
RUN python -c "from EasyAid.wsgi import application; print('WSGI import OK')"

# ЗАПУСК С МАКСИМАЛЬНЫМ ЛОГИРОВАНИЕМ
CMD echo "=== STARTING GUNICORN ===" && \
    echo "PORT: $PORT" && \
    echo "PWD: $(pwd)" && \
    echo "Files: $(ls -la)" && \
    gunicorn EasyAid.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 1 \
    --log-level debug \
    --access-logfile - \
    --error-logfile - \
    --capture-output \
    --enable-stdio-inheritance
'@ | Out-File Dockerfile -Encoding UTF8