FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=adoption.settings

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# project
COPY . /app/

# create media/static dirs
RUN mkdir -p /app/media /app/staticfiles

# collect static at build (ok for demo)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD sh -c "python manage.py migrate && gunicorn adoption.wsgi:application --bind 0.0.0.0:8000 --workers 3"