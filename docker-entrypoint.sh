#!/bin/sh

# Exit on any error
set -e

echo "🚀 Starting Yegna Farms deployment..."

# Activate virtual environment
. /app/venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

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
