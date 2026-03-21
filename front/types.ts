
export enum PropertyType {
  VILLA = 'Villa',
  APARTMENT = 'Apartment',
  MANSION = 'Mansion',
  PENTHOUSE = 'Penthouse',
  ESTATE = 'Estate'
}

export enum ListingStatus {
  FOR_SALE = 'For Sale',
  FOR_RENT = 'For Rent'
}

export interface Property {
  id: string | number;
  title: string;
  location: string;
  price: number;
  type: PropertyType;
  status: ListingStatus;
  beds: number;
  baths: number;
  sqft: number;
  description: string;
  images: string[];
  amenities: string[];
  coordinates: {
    lat: number;
    lng: number;
  };
}

export interface SearchFilters {
  query: string;
  type: PropertyType | 'All';
  status: ListingStatus | 'All';
  minPrice: number;
  maxPrice: number;
}
