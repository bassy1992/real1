# Bellerock Holdings - Backend API

Django REST API for the luxury real estate platform.

## Setup

1. Install dependencies:
```bash
pip3 install -r requirements.txt
```

2. Run migrations:
```bash
python3 manage.py migrate
```

3. Load initial property data:
```bash
python3 manage.py load_properties
```

4. Start the development server:
```bash
python3 manage.py runserver 8000
```

## API Endpoints

- `GET /api/properties/` - List all properties
- `GET /api/properties/{id}/` - Get property by ID
- `GET /api/properties/by_status/?status={status}` - Filter properties by status

## Admin Panel

Create a superuser to access the admin panel:
```bash
python3 manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin/
