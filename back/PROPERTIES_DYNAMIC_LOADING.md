# Properties Dynamic Loading Guide

## Overview
Properties are now fully loaded dynamically from the database. The system uses Django REST Framework on the backend and React with TypeScript on the frontend.

## Backend Setup

### Models
- `Property`: Main model storing property details (title, location, price, type, status, beds, baths, sqft, description, amenities, images, coordinates)
- `PropertyImage`: Model for storing additional uploaded images or image URLs

### API Endpoints
All endpoints are available at `http://127.0.0.1:8000/api/properties/`

1. **List all properties**: `GET /api/properties/`
   - Returns paginated list of all properties
   - Supports pagination: `?page=1&page_size=9`

2. **Get single property**: `GET /api/properties/{id}/`
   - Returns detailed information for a specific property

3. **Filter by status**: `GET /api/properties/by_status/?status={status}`
   - Filter properties by status (For Sale, For Rent)
   - Use `status=All` to get all properties

4. **Upload image**: `POST /api/properties/{id}/upload_image/`
   - Upload image file for a property
   - Supports both file uploads and URL-based images

5. **Add image URL**: `POST /api/properties/{id}/add_image_url/`
   - Add an image URL to a property

## Frontend Implementation

### Service Layer
`front/services/propertyService.ts` provides methods to interact with the API:
- `getAllProperties(page, pageSize)`: Fetch paginated properties
- `getPropertyById(id)`: Fetch single property
- `getPropertiesByStatus(status, page, pageSize)`: Filter by status

### Components
- `front/pages/Properties.tsx`: Main properties listing page
- `front/pages/Home.tsx`: Home page with featured properties (first 3)
- Both components use `useEffect` to fetch data on mount

## Loading Properties into Database

### Using Management Command
```bash
cd back
python manage.py load_properties
```

This command:
- Clears existing properties
- Loads 5 sample properties with images
- Creates PropertyImage entries for demonstration

### Manual Creation
You can also create properties through:
1. Django Admin: `http://127.0.0.1:8000/admin/`
2. Django REST Framework browsable API: `http://127.0.0.1:8000/api/properties/`
3. Direct API calls using tools like Postman or curl

## Data Flow

1. **Backend**: Django serves property data via REST API
2. **Frontend**: React components fetch data using `propertyService`
3. **State Management**: Properties stored in component state using `useState`
4. **Rendering**: Properties displayed dynamically based on fetched data

## Key Features

- **Pagination**: Backend supports pagination for large datasets
- **Filtering**: Filter properties by status (For Sale/For Rent)
- **Image Management**: Support for both URL-based and uploaded images
- **Real-time Updates**: Frontend fetches fresh data on component mount
- **Error Handling**: Proper error states and loading indicators

## Testing the Setup

1. Start the Django backend:
   ```bash
   cd back
   python manage.py runserver
   ```

2. Load sample data:
   ```bash
   python manage.py load_properties
   ```

3. Start the React frontend:
   ```bash
   cd front
   npm run dev
   ```

4. Visit `http://localhost:5173` to see properties loaded dynamically

## Adding New Properties

### Via Django Admin
1. Go to `http://127.0.0.1:8000/admin/`
2. Navigate to Properties
3. Click "Add Property"
4. Fill in the details and save

### Via API
```bash
curl -X POST http://127.0.0.1:8000/api/properties/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Property",
    "location": "City, Country",
    "price": 1000000,
    "property_type": "Villa",
    "status": "For Sale",
    "beds": 4,
    "baths": 3,
    "sqft": 3000,
    "description": "Beautiful property",
    "amenities": ["Pool", "Garden"],
    "images": ["https://example.com/image.jpg"],
    "latitude": 0.0,
    "longitude": 0.0
  }'
```

## Troubleshooting

### Properties not showing
- Check if backend is running: `http://127.0.0.1:8000/api/properties/`
- Verify database has properties: `python manage.py load_properties`
- Check browser console for API errors

### CORS Issues
- Ensure `django-cors-headers` is installed and configured in `settings.py`
- Check `CORS_ALLOWED_ORIGINS` includes your frontend URL

### Images not loading
- Verify image URLs are accessible
- Check `MEDIA_URL` and `MEDIA_ROOT` settings for uploaded images
- Ensure static files are properly configured
