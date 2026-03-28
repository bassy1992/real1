# 🗑️ Quick Guide: Auto-Delete Images from DigitalOcean Spaces

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│  Delete Image from Django Admin                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Django Signal Fires                                        │
│  (pre_delete signal)                                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Delete File from DigitalOcean Spaces                       │
│  (boto3 API call)                                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Delete Database Record                                     │
│  (Django ORM)                                               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Log Deletion                                               │
│  (post_delete signal)                                       │
└─────────────────────────────────────────────────────────────┘
```

## Usage

### Delete Single Image
1. Admin → Property Images
2. Select image
3. Click "Delete"
4. ✅ Both database record AND file deleted

### Delete Multiple Images
1. Admin → Property Images
2. Select multiple images (checkboxes)
3. Actions → "Delete selected"
4. ✅ All records AND files deleted

### Delete Property with Images
1. Admin → Properties
2. Select property
3. Click "Delete"
4. ✅ Property, all images, AND all files deleted

### Replace Image
1. Admin → Property Images
2. Select image
3. Upload new file
4. Click "Save"
5. ✅ Old file deleted, new file uploaded

## Configuration

### Required Environment Variables (Railway)

```bash
USE_SPACES=True
DO_SPACES_KEY=DO8014PDYEMPMGC8CMYR
DO_SPACES_SECRET=MRio2V3xaCvUMJXWwGmzAjfJceHIggO1EH4ripqy5j8
DO_SPACES_BUCKET_NAME=lutheran
DO_SPACES_ENDPOINT_URL=https://sfo3.digitaloceanspaces.com
DO_SPACES_REGION=sfo3
DO_SPACES_CDN_DOMAIN=lutheran.sfo3.cdn.digitaloceanspaces.com
```

## Testing

### Quick Test

```bash
cd back
python test_image_deletion.py
```

### Manual Test

1. Upload test image
2. Note URL: `https://lutheran.sfo3.cdn.digitaloceanspaces.com/media/properties/...`
3. Delete image from admin
4. Try URL → Should return 404 ✅

## What Gets Deleted?

| Type | Deleted from DB | Deleted from DO Spaces |
|------|----------------|------------------------|
| Uploaded Image | ✅ Yes | ✅ Yes |
| External URL | ✅ Yes | ❌ No (not stored there) |

## Monitoring

Check Railway logs:

```bash
railway logs
```

Look for:
```
INFO: Deleted image from Spaces: properties/2026/03/28/image.jpg
INFO: PropertyImage deleted: Property Name - Image 1
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Images not deleting | Check Railway logs for errors |
| Permission denied | Verify DO_SPACES_KEY and SECRET |
| Signal not firing | Restart Django server |

## Benefits

✅ No orphaned files  
✅ Automatic cleanup  
✅ Cost savings  
✅ Storage optimization  
✅ No manual management  

## Documentation

- Full guide: `IMAGE_DELETION_GUIDE.md`
- Summary: `DO_SPACES_AUTO_DELETE_SUMMARY.md`
- Test script: `test_image_deletion.py`

---

**Status:** ✅ Active and working
