"""
Example script demonstrating how to upload images to properties
Run this after starting the Django server
"""

import requests

BASE_URL = "http://localhost:8000/api"

def upload_image_file(property_id, image_path, caption="", order=0):
    """Upload an image file to a property"""
    url = f"{BASE_URL}/properties/{property_id}/upload_image/"
    
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        data = {
            'caption': caption,
            'order': order
        }
        response = requests.post(url, files=files, data=data)
    
    if response.status_code == 201:
        print(f"✓ Image uploaded successfully: {response.json()}")
    else:
        print(f"✗ Error uploading image: {response.status_code} - {response.text}")
    
    return response.json() if response.status_code == 201 else None


def add_image_url(property_id, image_url, caption="", order=0):
    """Add an image URL to a property"""
    url = f"{BASE_URL}/properties/{property_id}/add_image_url/"
    
    data = {
        'url': image_url,
        'caption': caption,
        'order': order
    }
    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        print(f"✓ Image URL added successfully: {response.json()}")
    else:
        print(f"✗ Error adding image URL: {response.status_code} - {response.text}")
    
    return response.json() if response.status_code == 201 else None


def get_property(property_id):
    """Get property details including all images"""
    url = f"{BASE_URL}/properties/{property_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        property_data = response.json()
        print(f"\nProperty: {property_data['title']}")
        print(f"All images: {len(property_data['all_images'])} total")
        for idx, img in enumerate(property_data['all_images'], 1):
            print(f"  {idx}. {img}")
    else:
        print(f"✗ Error getting property: {response.status_code}")
    
    return response.json() if response.status_code == 200 else None


if __name__ == "__main__":
    print("=== Property Image Upload Examples ===\n")
    
    # Example 1: Add an image URL
    print("1. Adding image URL to property 1...")
    add_image_url(
        property_id=1,
        image_url="https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
        caption="Beautiful exterior view",
        order=10
    )
    
    # Example 2: Upload a file (uncomment if you have an image file)
    # print("\n2. Uploading image file to property 1...")
    # upload_image_file(
    #     property_id=1,
    #     image_path="path/to/your/image.jpg",
    #     caption="Interior shot",
    #     order=11
    # )
    
    # Example 3: Get property with all images
    print("\n3. Fetching property details...")
    get_property(property_id=1)
