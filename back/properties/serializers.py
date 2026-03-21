from rest_framework import serializers
from .models import Property, PropertyImage


class PropertyImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'url', 'image_url', 'caption', 'order']
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.get_image_url()
        if image_url and request and not image_url.startswith('http'):
            return request.build_absolute_uri(image_url)
        return image_url


class PropertySerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='property_type')
    coordinates = serializers.SerializerMethodField()
    uploaded_images = PropertyImageSerializer(many=True, read_only=True)
    all_images = serializers.SerializerMethodField()
    
    class Meta:
        model = Property
        fields = ['id', 'title', 'location', 'price', 'type', 'status', 
                  'beds', 'baths', 'sqft', 'description', 'amenities', 
                  'images', 'uploaded_images', 'all_images', 'coordinates']
    
    def get_coordinates(self, obj):
        return {
            'lat': obj.latitude,
            'lng': obj.longitude
        }
    
    def get_all_images(self, obj):
        """Combine URL-based images and uploaded images"""
        request = self.context.get('request')
        all_imgs = []
        
        # Add URL-based images from JSON field
        for url in obj.images:
            all_imgs.append(url)
        
        # Add uploaded images
        for img in obj.uploaded_images.all():
            img_url = img.get_image_url()
            if img_url and request and not img_url.startswith('http'):
                img_url = request.build_absolute_uri(img_url)
            all_imgs.append(img_url)
        
        return all_imgs
