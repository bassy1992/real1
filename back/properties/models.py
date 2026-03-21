from django.db import models


class Property(models.Model):
    PROPERTY_TYPES = [
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment'),
        ('Mansion', 'Mansion'),
        ('Penthouse', 'Penthouse'),
        ('Estate', 'Estate'),
    ]
    
    LISTING_STATUS = [
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
    ]
    
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    status = models.CharField(max_length=50, choices=LISTING_STATUS)
    beds = models.IntegerField()
    baths = models.IntegerField()
    sqft = models.IntegerField()
    description = models.TextField()
    amenities = models.JSONField(default=list)
    images = models.JSONField(default=list)  # Keep for backward compatibility with URLs
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-created_at']


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='uploaded_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    url = models.URLField(max_length=500, blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return f"{self.property.title} - Image {self.order}"
    
    def get_image_url(self):
        """Return the image URL whether it's uploaded or external"""
        if self.image:
            return self.image.url
        return self.url or ''
