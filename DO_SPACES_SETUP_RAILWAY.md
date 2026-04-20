# DigitalOcean Spaces Setup for Railway

## Environment Variables to Add in Railway

Go to your Railway service → Variables tab and add these:

```
USE_SPACES=True
DO_SPACES_KEY=DO8014PDYEMPMGC8CMYR
DO_SPACES_SECRET=MRio2V3xaCvUMJXWwGmzAjfJceHIggO1EH4ripqy5j8
DO_SPACES_BUCKET_NAME=lutheran
DO_SPACES_ENDPOINT_URL=https://sfo3.digitaloceanspaces.com
DO_SPACES_REGION=sfo3
DO_SPACES_CDN_DOMAIN=lutheran.sfo3.cdn.digitaloceanspaces.com
```

## What This Does

Once configured, your Django app will:
- Upload all property images to DigitalOcean Spaces
- Serve images via CDN: `https://lutheran.sfo3.cdn.digitaloceanspaces.com/media/`
- Automatically delete images from Spaces when properties are deleted
- Handle image uploads through the Django admin

## Testing

After Railway redeploys:
1. Go to Django admin: `https://web-production-1409f.up.railway.app/admin/`
2. Create or edit a property
3. Upload an image
4. The image will be stored in DigitalOcean Spaces
5. Check your DO Spaces dashboard to verify the upload

## CORS Configuration in DigitalOcean Spaces

Make sure your Spaces bucket has CORS enabled:

1. Go to DigitalOcean → Spaces → lutheran bucket
2. Click "Settings" tab
3. Add CORS configuration:

```xml
<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>https://www.bellrockholdings.org</AllowedOrigin>
        <AllowedOrigin>https://bellrockholdings.org</AllowedOrigin>
        <AllowedOrigin>https://web-production-1409f.up.railway.app</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>DELETE</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

## File Structure in Spaces

Images will be organized as:
```
media/
  properties/
    2026/
      04/
        20/
          image1.jpg
          image2.jpg
```

## Troubleshooting

### Images not uploading
- Check Railway logs for boto3 errors
- Verify DO Spaces credentials are correct
- Ensure bucket exists and is accessible

### Images not displaying
- Check CORS configuration in DO Spaces
- Verify CDN domain is correct
- Check browser console for CORS errors

### Images not deleting
- Check that signals are working (see logs)
- Verify AWS_DEFAULT_ACL is set to 'public-read'
