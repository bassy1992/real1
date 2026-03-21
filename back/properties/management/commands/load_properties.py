from django.core.management.base import BaseCommand
from properties.models import Property, PropertyImage


class Command(BaseCommand):
    help = 'Load initial property data'

    def handle(self, *args, **kwargs):
        Property.objects.all().delete()
        
        properties_data = [
            {
                'title': 'Azure Bay Villa',
                'location': 'Malibu, California',
                'price': 12500000,
                'property_type': 'Villa',
                'status': 'For Sale',
                'beds': 6,
                'baths': 7,
                'sqft': 8500,
                'description': 'A breathtaking oceanfront estate with panoramic Pacific views and a private beach access. Features floor-to-ceiling windows and premium finishes.',
                'images': [
                    'https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1613977257363-707ba9348227?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600607687940-c52df0d43739?auto=format&fit=crop&q=80&w=1200'
                ],
                'amenities': ['Infinity Pool', 'Home Theater', 'Wine Cellar', 'Smart Home System'],
                'latitude': 34.0259,
                'longitude': -118.7798
            },
            {
                'title': 'Skyline Penthouse',
                'location': 'Manhattan, New York',
                'price': 45000,
                'property_type': 'Penthouse',
                'status': 'For Rent',
                'beds': 3,
                'baths': 3,
                'sqft': 3200,
                'description': 'Ultra-modern penthouse featuring double-height ceilings and a wrap-around terrace overlooking Central Park. Experience the pinnacle of NYC living.',
                'images': [
                    'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600607687644-c7171b42398b?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600566753190-17f0bb2a6c3e?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1200'
                ],
                'amenities': ['Private Elevator', 'Gym', '24/7 Concierge', 'Rooftop Garden'],
                'latitude': 40.7831,
                'longitude': -73.9712
            },
            {
                'title': 'Cotswold Manor',
                'location': 'Oxfordshire, United Kingdom',
                'price': 8900000,
                'property_type': 'Mansion',
                'status': 'For Sale',
                'beds': 8,
                'baths': 6,
                'sqft': 12000,
                'description': 'A historic 17th-century manor meticulously restored with modern luxuries and vast equestrian grounds. Traditional charm meets contemporary elegance.',
                'images': [
                    'https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600585154526-990dcea4db0d?auto=format&fit=crop&q=80&w=1200'
                ],
                'amenities': ['Stable', 'Grand Ballroom', 'Tennis Court', 'Library'],
                'latitude': 51.7520,
                'longitude': -1.2577
            },
            {
                'title': 'Oasis Desert Estate',
                'location': 'Dubai, UAE',
                'price': 25000000,
                'property_type': 'Estate',
                'status': 'For Sale',
                'beds': 10,
                'baths': 12,
                'sqft': 22000,
                'description': 'Architectural masterpiece in the heart of the desert, featuring climate-controlled indoor gardens and a custom art gallery space.',
                'images': [
                    'https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600607687940-c52df0d43739?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600573472591-ee6b68d14c68?auto=format&fit=crop&q=80&w=1200'
                ],
                'amenities': ['Helipad', 'Indoor Garden', 'Private Spa', 'Olympic Pool'],
                'latitude': 25.2048,
                'longitude': 55.2708
            },
            {
                'title': 'Riviera Glass House',
                'location': 'Nice, France',
                'price': 15000,
                'property_type': 'Villa',
                'status': 'For Rent',
                'beds': 4,
                'baths': 4,
                'sqft': 4500,
                'description': 'Minimalist glass-walled villa perched on the cliffs of the French Riviera with 360-degree views of the Mediterranean Sea.',
                'images': [
                    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?auto=format&fit=crop&q=80&w=1200',
                    'https://images.unsplash.com/photo-1600585154526-990dcea4db0d?auto=format&fit=crop&q=80&w=1200'
                ],
                'amenities': ['Ocean View', 'Outdoor Kitchen', 'Guest House', 'Security System'],
                'latitude': 43.7102,
                'longitude': 7.2620
            }
        ]
        
        for data in properties_data:
            Property.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(properties_data)} properties'))
        
        # Example: Create PropertyImage entries from URLs for the first property
        first_property = Property.objects.first()
        if first_property:
            for idx, img_url in enumerate(first_property.images[:2]):
                PropertyImage.objects.create(
                    property=first_property,
                    url=img_url,
                    order=idx
                )
            self.stdout.write(self.style.SUCCESS(f'Created {2} PropertyImage entries for {first_property.title}'))
