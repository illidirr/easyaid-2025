FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
CMD python -c "import os; print('Starting on port', os.environ.get('PORT', 8000)); import time; time.sleep(300)"