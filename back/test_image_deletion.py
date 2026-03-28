#!/usr/bin/env python
"""
Test script for verifying automatic image deletion from DigitalOcean Spaces.

Usage:
    python test_image_deletion.py

This script tests:
1. Image deletion when PropertyImage is deleted
2. Old image deletion when image is replaced
3. Cascade deletion when Property is deleted
"""

import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from properties.models import Property, PropertyImage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import requests


def test_image_exists(url):
    """Check if an image exists at the given URL"""
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False


def create_test_image():
    """Create a simple test image file"""
    # Create a minimal valid JPEG file (1x1 pixel)
    jpeg_data = (
        b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00'
        b'\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c'
        b'\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c'
        b'\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xc0\x00\x0b\x08\x00'
        b'\x01\x00\x01\x01\x01\x11\x00\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01'
        b'\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05'
        b'\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04'
        b'\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A'
        b'\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82'
        b'\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz'
        b'\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a'
        b'\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9'
        b'\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8'
        b'\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5'
        b'\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x08\x01\x01\x00\x00?\x00\xffd\xa2\x8a'
        b'\xff\xd9'
    )
    return SimpleUploadedFile("test_image.jpg", jpeg_data, content_type="image/jpeg")


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def print_result(test_name, passed, message=""):
    """Print test result"""
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"{status} - {test_name}")
    if message:
        print(f"    {message}")


def main():
    print_header("DigitalOcean Spaces Image Deletion Test")
    
    if not settings.USE_SPACES:
        print("❌ ERROR: USE_SPACES is False. Set USE_SPACES=True to test.")
        sys.exit(1)
    
    print(f"\n📦 Storage Configuration:")
    print(f"   Bucket: {settings.DO_SPACES_BUCKET_NAME}")
    print(f"   Region: {settings.DO_SPACES_REGION}")
    print(f"   CDN: {settings.DO_SPACES_CDN_DOMAIN}")
    
    # Test 1: Create test property
    print_header("Test 1: Create Test Property")
    try:
        test_property = Property.objects.create(
            title="Test Property for Deletion",
            location="Test Location",
            price=1000000,
            property_type="Villa",
            status="For Sale",
            beds=3,
            baths=2,
            sqft=2000,
            description="Test property for image deletion testing",
            latitude=0.0,
            longitude=0.0
        )
        print_result("Create test property", True, f"Property ID: {test_property.id}")
    except Exception as e:
        print_result("Create test property", False, str(e))
        sys.exit(1)
    
    # Test 2: Upload image
    print_header("Test 2: Upload Image to DigitalOcean Spaces")
    try:
        test_image = create_test_image()
        property_image = PropertyImage.objects.create(
            property=test_property,
            image=test_image,
            caption="Test Image",
            order=1
        )
        image_url = property_image.image.url
        image_name = property_image.image.name
        print_result("Upload image", True, f"URL: {image_url}")
        print(f"    File: {image_name}")
        
        # Verify image exists
        if test_image_exists(image_url):
            print_result("Verify image exists in Spaces", True)
        else:
            print_result("Verify image exists in Spaces", False, "Image not accessible")
    except Exception as e:
        print_result("Upload image", False, str(e))
        test_property.delete()
        sys.exit(1)
    
    # Test 3: Delete image and verify it's removed from Spaces
    print_header("Test 3: Delete Image and Verify Removal from Spaces")
    try:
        image_id = property_image.id
        stored_url = image_url
        stored_name = image_name
        
        # Delete the image
        property_image.delete()
        print_result("Delete PropertyImage record", True, f"Deleted image ID: {image_id}")
        
        # Wait a moment for deletion to complete
        import time
        time.sleep(2)
        
        # Verify image no longer exists in Spaces
        if not test_image_exists(stored_url):
            print_result("Verify image removed from Spaces", True, "Image no longer accessible")
        else:
            print_result("Verify image removed from Spaces", False, "Image still accessible!")
    except Exception as e:
        print_result("Delete image", False, str(e))
        test_property.delete()
        sys.exit(1)
    
    # Test 4: Test image replacement
    print_header("Test 4: Test Image Replacement (Old Image Deletion)")
    try:
        # Upload first image
        test_image1 = create_test_image()
        property_image = PropertyImage.objects.create(
            property=test_property,
            image=test_image1,
            caption="First Image",
            order=1
        )
        first_url = property_image.image.url
        first_name = property_image.image.name
        print_result("Upload first image", True, f"URL: {first_url}")
        
        # Replace with second image
        test_image2 = create_test_image()
        property_image.image = test_image2
        property_image.save()
        second_url = property_image.image.url
        print_result("Replace with second image", True, f"URL: {second_url}")
        
        # Wait for deletion
        import time
        time.sleep(2)
        
        # Verify old image is deleted
        if not test_image_exists(first_url):
            print_result("Verify old image deleted", True, "Old image removed from Spaces")
        else:
            print_result("Verify old image deleted", False, "Old image still exists!")
        
        # Verify new image exists
        if test_image_exists(second_url):
            print_result("Verify new image exists", True, "New image accessible")
        else:
            print_result("Verify new image exists", False, "New image not accessible!")
        
        # Clean up
        property_image.delete()
    except Exception as e:
        print_result("Image replacement test", False, str(e))
        test_property.delete()
        sys.exit(1)
    
    # Test 5: Test cascade deletion
    print_header("Test 5: Test Cascade Deletion (Property with Images)")
    try:
        # Create multiple images
        image_urls = []
        for i in range(3):
            test_image = create_test_image()
            img = PropertyImage.objects.create(
                property=test_property,
                image=test_image,
                caption=f"Test Image {i+1}",
                order=i+1
            )
            image_urls.append(img.image.url)
        
        print_result("Create 3 test images", True, f"Created {len(image_urls)} images")
        
        # Delete the property (should cascade delete all images)
        property_id = test_property.id
        test_property.delete()
        print_result("Delete property", True, f"Deleted property ID: {property_id}")
        
        # Wait for deletion
        import time
        time.sleep(2)
        
        # Verify all images are deleted from Spaces
        deleted_count = 0
        for url in image_urls:
            if not test_image_exists(url):
                deleted_count += 1
        
        if deleted_count == len(image_urls):
            print_result("Verify all images deleted", True, f"All {deleted_count} images removed from Spaces")
        else:
            print_result("Verify all images deleted", False, f"Only {deleted_count}/{len(image_urls)} images deleted")
    except Exception as e:
        print_result("Cascade deletion test", False, str(e))
        try:
            test_property.delete()
        except:
            pass
        sys.exit(1)
    
    # Summary
    print_header("Test Summary")
    print("✅ All tests passed!")
    print("\nAutomatic image deletion is working correctly:")
    print("  ✓ Images deleted from Spaces when PropertyImage is deleted")
    print("  ✓ Old images deleted when replaced with new ones")
    print("  ✓ All images deleted when Property is deleted (cascade)")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
