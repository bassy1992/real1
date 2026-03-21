#!/bin/bash

echo "=== Setting up Property Image Upload System ==="
echo ""

# Install dependencies
echo "1. Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo ""
echo "2. Running migrations..."
python manage.py migrate

# Load sample data
echo ""
echo "3. Loading sample properties..."
python manage.py load_properties

# Create media directory
echo ""
echo "4. Creating media directory..."
mkdir -p media/properties

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "Next steps:"
echo "1. Start the server: python manage.py runserver"
echo "2. Test the API using the example script: python example_upload.py"
echo "3. Or access the admin interface at: http://localhost:8000/admin/"
echo ""
echo "See IMAGE_UPLOAD_GUIDE.md for detailed documentation."
