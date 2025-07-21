#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Yegna Farms deployment..."

# Function to wait for database (if using external DB)
wait_for_db() {
    echo "⏳ Waiting for database to be ready..."
    python << END
import sys
import time
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yegna_portfolio.settings')
django.setup()

from django.db import connections
from django.db.utils import OperationalError

db_conn = connections['default']
retries = 30
while retries > 0:
    try:
        db_conn.ensure_connection()
        break
    except OperationalError:
        retries -= 1
        print(f"Database unavailable, waiting... ({retries} retries left)")
        time.sleep(2)

if retries == 0:
    print("❌ Database connection failed!")
    sys.exit(1)

print("✅ Database connection successful!")
END
}

# Wait for database
wait_for_db

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Seed database if needed
echo "🌱 Seeding database with initial data..."
python manage.py seed_production_data

# Run system checks
echo "🔍 Running system checks..."
python manage.py check --deploy

echo "✅ Deployment preparation complete!"

# Start the application
echo "🌟 Starting Yegna Farms application..."
exec "$@"
