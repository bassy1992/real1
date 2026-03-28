
import { Property, PropertyType, ListingStatus } from './types';

export const MOCK_PROPERTIES: Property[] = [
  {
    id: '1',
    title: 'Azure Bay Villa',
    location: 'Malibu, California',
    price: 12500000,
    type: PropertyType.VILLA,
    status: ListingStatus.FOR_SALE,
    beds: 6,
    baths: 7,
    sqft: 8500,
    description: 'A breathtaking oceanfront estate with panoramic Pacific views and a private beach access. Features floor-to-ceiling windows and premium finishes.',
    images: [
      'https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1613977257363-707ba9348227?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600607687940-c52df0d43739?auto=format&fit=crop&q=80&w=1200'
    ],
    amenities: ['Infinity Pool', 'Home Theater', 'Wine Cellar', 'Smart Home System'],
    coordinates: { lat: 34.0259, lng: -118.7798 }
  },
  {
    id: '2',
    title: 'Skyline Penthouse',
    location: 'Manhattan, New York',
    price: 45000,
    type: PropertyType.PENTHOUSE,
    status: ListingStatus.FOR_RENT,
    beds: 3,
    baths: 3.5,
    sqft: 3200,
    description: 'Ultra-modern penthouse featuring double-height ceilings and a wrap-around terrace overlooking Central Park. Experience the pinnacle of NYC living.',
    images: [
      'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600607687644-c7171b42398b?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600566753190-17f0bb2a6c3e?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1200'
    ],
    amenities: ['Private Elevator', 'Gym', '24/7 Concierge', 'Rooftop Garden'],
    coordinates: { lat: 40.7831, lng: -73.9712 }
  },
  {
    id: '3',
    title: 'Cotswold Manor',
    location: 'Oxfordshire, United Kingdom',
    price: 8900000,
    type: PropertyType.MANSION,
    status: ListingStatus.FOR_SALE,
    beds: 8,
    baths: 6,
    sqft: 12000,
    description: 'A historic 17th-century manor meticulously restored with modern luxuries and vast equestrian grounds. Traditional charm meets contemporary elegance.',
    images: [
      'https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600585154526-990dcea4db0d?auto=format&fit=crop&q=80&w=1200'
    ],
    amenities: ['Stable', 'Grand Ballroom', 'Tennis Court', 'Library'],
    coordinates: { lat: 51.7520, lng: -1.2577 }
  },
  {
    id: '4',
    title: 'Oasis Desert Estate',
    location: 'Dubai, UAE',
    price: 25000000,
    type: PropertyType.ESTATE,
    status: ListingStatus.FOR_SALE,
    beds: 10,
    baths: 12,
    sqft: 22000,
    description: 'Architectural masterpiece in the heart of the desert, featuring climate-controlled indoor gardens and a custom art gallery space.',
    images: [
      'https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600607687940-c52df0d43739?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600573472591-ee6b68d14c68?auto=format&fit=crop&q=80&w=1200'
    ],
    amenities: ['Helipad', 'Indoor Garden', 'Private Spa', 'Olympic Pool'],
    coordinates: { lat: 25.2048, lng: 55.2708 }
  },
  {
    id: '5',
    title: 'Riviera Glass House',
    location: 'Nice, France',
    price: 15000,
    type: PropertyType.VILLA,
    status: ListingStatus.FOR_RENT,
    beds: 4,
    baths: 4,
    sqft: 4500,
    description: 'Minimalist glass-walled villa perched on the cliffs of the French Riviera with 360-degree views of the Mediterranean Sea.',
    images: [
      'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?auto=format&fit=crop&q=80&w=1200',
      'https://images.unsplash.com/photo-1600585154526-990dcea4db0d?auto=format&fit=crop&q=80&w=1200'
    ],
    amenities: ['Ocean View', 'Outdoor Kitchen', 'Guest House', 'Security System'],
    coordinates: { lat: 43.7102, lng: 7.2620 }
  }
];

export const COLORS = {
  NAVY: '#050a14',
  NAVY_LIGHT: '#101827',
  GOLD: '#d4af37',
  GOLD_HOVER: '#f1c40f',
  SILVER: '#c0c0c0',
  WHITE: '#f8fafc'
};

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://real-production-4319.up.railway.app/api';
