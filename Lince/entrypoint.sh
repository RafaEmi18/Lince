#!/bin/bash

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
until python -c "import psycopg2; psycopg2.connect(host='db', port=5432, user='django_user', password='django_pass', dbname='django_db')" 2>/dev/null; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done
echo "PostgreSQL started"

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist (optional)
# python manage.py createsuperuser --noinput || true

# Start server
echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000

