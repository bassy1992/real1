# DigitalOcean Spaces Configuration Guide

## Overview
The application is now configured to use DigitalOcean Spaces for media file storage (uploaded images). This provides scalable, reliable cloud storage with CDN delivery.

## Configuration Details

### DigitalOcean Spaces Settings
- **Bucket Name**: lutheran
- **Region**: sfo3 (San Francisco 3)
- **Endpoint**: https://sfo3.digitaloceanspaces.com
- **CDN Domain**: lutheran.sfo3.cdn.digitaloceanspaces.com

### Environment Variables
The following settings are configured in `backend/settings.py`:

```python
USE_SPACES = True
DO_SPACES_KEY = 'DO8014PDYEMPMGC8CMYR'
DO_SPACES_SECRET = 'MRio2V3xaCvUMJXWwGmzAjfJceHIggO1EH4ripqy5j8'
DO_SPACES_BUCKET_NAME = 'lutheran'
DO_SPACES_ENDPOINT_URL = 'https://sfo3.digitaloceanspaces.com'
DO_SPACES_REGION = 'sfo3'
DO_SPACES_CDN_DOMAIN = 'lutheran.sfo3.cdn.digitaloceanspaces.com'
```

## How It Works

### File Upload Flow
1. User uploads an image through the API or Django Admin
2. Django processes the upload using `django-storages` with `boto3`
3. File is automatically uploaded to DigitalOcean Spaces
4. File URL is generated using the CDN domain for fast delivery
5. URL is stored in the database and returned to the frontend

### Storage Backend
- **Library**: `django-storages` with S3-compatible backend
- **AWS SDK**: `boto3` (DigitalOcean Spaces is S3-compatible)
- **Default Storage**: `storages.backends.s3boto3.S3Boto3Storage`

### File Settings
- **Location**: Files are stored in the `media/` folder within the bucket
- **ACL**: `public-read` (files are publicly accessible)
- **Cache Control**: `max-age=86400` (24 hours)
- **File Overwrite**: Disabled (preserves original files)
- **Query String Auth**: Disabled (no signed URLs needed for public files)

## Switching Between Local and Cloud Storage

### Use DigitalOcean Spaces (Production)
```python
USE_SPACES = True
```

### Use Local Storage (Development)
```python
USE_SPACES = False
```

When `USE_SPACES = False`, files are stored locally in `back/media/` directory.

## Testing the Configuration

### 1. Upload via Django Admin
```bash
cd back
python3 manage.py runserver
```
- Go to http://127.0.0.1:8000/admin/
- Navigate to Properties or Property Images
- Upload an image
- Check that the image URL uses the CDN domain

### 2. Upload via API
```bash
curl -X POST http://127.0.0.1:8000/api/properties/1/upload_image/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@/path/to/image.jpg" \
  -F "caption=Test Image"
```

### 3. Verify in DigitalOcean
- Log into DigitalOcean Console
- Navigate to Spaces
- Open the `lutheran` bucket
- Check the `media/` folder for uploaded files

## Security Best Practices

### For Production
1. **Move credentials to environment variables**:
   ```python
   import os
   
   DO_SPACES_KEY = os.environ.get('DO_SPACES_KEY')
   DO_SPACES_SECRET = os.environ.get('DO_SPACES_SECRET')
   ```

2. **Use `.env` file** (with `python-decouple` or `django-environ`):
   ```bash
   pip install python-decouple
   ```
   
   Create `.env` file:
   ```
   DO_SPACES_KEY=DO8014PDYEMPMGC8CMYR
   DO_SPACES_SECRET=MRio2V3xaCvUMJXWwGmzAjfJceHIggO1EH4ripqy5j8
   ```
   
   Update settings.py:
   ```python
   from decouple import config
   
   DO_SPACES_KEY = config('DO_SPACES_KEY')
   DO_SPACES_SECRET = config('DO_SPACES_SECRET')
   ```

3. **Add `.env` to `.gitignore`** to prevent committing credentials

## Troubleshooting

### Images not uploading
- Check DigitalOcean Spaces credentials are correct
- Verify bucket name and region match
- Ensure `boto3` and `django-storages` are installed
- Check bucket permissions allow public read access

### Images not displaying
- Verify CDN domain is correct
- Check CORS settings in DigitalOcean Spaces
- Ensure files have `public-read` ACL

### CORS Configuration in DigitalOcean
If images don't load in the browser, add CORS rules in DigitalOcean Spaces:

1. Go to Spaces settings
2. Add CORS configuration:
```json
[
  {
    "AllowedOrigins": ["*"],
    "AllowedMethods": ["GET", "HEAD"],
    "AllowedHeaders": ["*"],
    "MaxAgeSeconds": 3000
  }
]
```

## File Structure

### Uploaded Files Location
```
lutheran (bucket)
└── media/
    ├── property_images/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    └── investment_images/
        ├── image1.jpg
        └── ...
```

### URL Format
```
https://lutheran.sfo3.cdn.digitaloceanspaces.com/media/property_images/image1.jpg
```

## Benefits

1. **Scalability**: Handle unlimited file uploads without server storage limits
2. **Performance**: CDN delivery ensures fast image loading globally
3. **Reliability**: DigitalOcean's infrastructure provides high availability
4. **Cost-Effective**: Pay only for storage and bandwidth used
5. **Backup**: Files are automatically backed up by DigitalOcean

## Migration from Local Storage

If you have existing files in `back/media/`, you can migrate them:

```bash
# Install AWS CLI or use DigitalOcean's web interface
# Upload files to the bucket maintaining the same structure
aws s3 sync back/media/ s3://lutheran/media/ \
  --endpoint-url=https://sfo3.digitaloceanspaces.com \
  --acl public-read
```

## Monitoring

### Check Storage Usage
- DigitalOcean Console → Spaces → lutheran
- View storage size and bandwidth usage
- Monitor costs in billing section

### File Management
- Use DigitalOcean Console to browse, delete, or manage files
- Set up lifecycle policies for automatic cleanup if needed
