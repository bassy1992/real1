# Property Image Upload Guide

This guide explains how to load property images using both URLs and file uploads.

## Features

- **URL-based images**: Store external image URLs (e.g., from Unsplash, CDN)
- **File uploads**: Upload image files directly to the server
- **Mixed approach**: Use both methods for the same property
- **Image ordering**: Control the display order of images
- **Captions**: Add optional captions to images

## Setup

### 1. Install Dependencies

```bash
cd back
pip install -r requirements.txt
```

This will install Pillow, required for image processing.

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Load Sample Data

```bash
python manage.py load_properties
```

### 4. Create Media Directory

The media directory will be created automatically when you upload your first image, but you can create it manually:

```bash
mkdir -p media/properties
```

## API Endpoints

### 1. Upload Image File

**Endpoint**: `POST /api/properties/{id}/upload_image/`

**Content-Type**: `multipart/form-data`

**Parameters**:
- `image` (file, optional): The image file to upload
- `url` (string, optional): External image URL
- `caption` (string, optional): Image caption
- `order` (integer, optional): Display order (default: 0)

**Note**: Either `image` or `url` must be provided.

**Example using curl**:
```bash
curl -X POST http://localhost:8000/api/properties/1/upload_image/ \
  -F "image=@/path/to/image.jpg" \
  -F "caption=Beautiful view" \
  -F "order=1"
```

**Example using Python**:
```python
import requests

url = "http://localhost:8000/api/properties/1/upload_image/"
files = {'image': open('image.jpg', 'rb')}
data = {'caption': 'Beautiful view', 'order': 1}
response = requests.post(url, files=files, data=data)
```

### 2. Add Image URL

**Endpoint**: `POST /api/properties/{id}/add_image_url/`

**Content-Type**: `application/json`

**Parameters**:
- `url` (string, required): External image URL
- `caption` (string, optional): Image caption
- `order` (integer, optional): Display order (default: 0)

**Example using curl**:
```bash
curl -X POST http://localhost:8000/api/properties/1/add_image_url/ \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
    "caption": "Exterior view",
    "order": 2
  }'
```

**Example using Python**:
```python
import requests

url = "http://localhost:8000/api/properties/1/add_image_url/"
data = {
    'url': 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c',
    'caption': 'Exterior view',
    'order': 2
}
response = requests.post(url, json=data)
```

### 3. Get Property with Images

**Endpoint**: `GET /api/properties/{id}/`

**Response includes**:
- `images`: Array of URL-based images (legacy JSON field)
- `uploaded_images`: Array of PropertyImage objects with details
- `all_images`: Combined array of all image URLs (both sources)

**Example**:
```bash
curl http://localhost:8000/api/properties/1/
```

**Response**:
```json
{
  "id": 1,
  "title": "Azure Bay Villa",
  "images": ["https://..."],
  "uploaded_images": [
    {
      "id": 1,
      "image": "/media/properties/2024/03/18/image.jpg",
      "url": null,
      "image_url": "http://localhost:8000/media/properties/2024/03/18/image.jpg",
      "caption": "Beautiful view",
      "order": 1
    }
  ],
  "all_images": [
    "https://...",
    "http://localhost:8000/media/properties/2024/03/18/image.jpg"
  ]
}
```

## Models

### Property Model
- Keeps the existing `images` JSONField for backward compatibility
- Related to PropertyImage via `uploaded_images`

### PropertyImage Model
- `property`: ForeignKey to Property
- `image`: ImageField for uploaded files (optional)
- `url`: URLField for external URLs (optional)
- `caption`: Optional caption text
- `order`: Integer for sorting
- `created_at`: Timestamp

## Frontend Integration

### Using fetch API

```javascript
// Upload file
const formData = new FormData();
formData.append('image', fileInput.files[0]);
formData.append('caption', 'Beautiful view');
formData.append('order', 1);

fetch(`http://localhost:8000/api/properties/1/upload_image/`, {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log('Success:', data));

// Add URL
fetch(`http://localhost:8000/api/properties/1/add_image_url/`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    url: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c',
    caption: 'Exterior view',
    order: 2
  })
})
.then(response => response.json())
.then(data => console.log('Success:', data));
```

## Testing

Run the example script:

```bash
cd back
python example_upload.py
```

## Admin Interface

Access the Django admin at `http://localhost:8000/admin/` to:
- View and manage PropertyImage entries
- Upload images directly through the admin interface
- Edit image captions and ordering
- See inline images when editing properties

## Notes

- Uploaded images are stored in `media/properties/YYYY/MM/DD/`
- The `all_images` field combines both URL-based and uploaded images
- Images are ordered by the `order` field, then by creation date
- Both `image` and `url` fields are optional, but at least one must be provided
