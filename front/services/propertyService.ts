import { Property } from '../types';
import { API_BASE_URL } from '../constants';

interface PaginatedResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Property[];
}

export const propertyService = {
  async getAllProperties(page: number = 1, pageSize: number = 9): Promise<Property[]> {
    const response = await fetch(`${API_BASE_URL}/properties/?page=${page}&page_size=${pageSize}`);
    if (!response.ok) {
      throw new Error('Failed to fetch properties');
    }
    const data = await response.json();
    // Handle both paginated and non-paginated responses
    return Array.isArray(data) ? data : data.results;
  },

  async getPropertyById(id: string): Promise<Property> {
    const response = await fetch(`${API_BASE_URL}/properties/${id}/`);
    if (!response.ok) {
      throw new Error('Failed to fetch property');
    }
    return response.json();
  },

  async getPropertiesByStatus(status: string, page: number = 1, pageSize: number = 9): Promise<Property[]> {
    const response = await fetch(`${API_BASE_URL}/properties/by_status/?status=${status}&page=${page}&page_size=${pageSize}`);
    if (!response.ok) {
      throw new Error('Failed to fetch properties');
    }
    const data = await response.json();
    return Array.isArray(data) ? data : data.results;
  },

  async getPropertiesByType(type: string, page: number = 1, pageSize: number = 9): Promise<Property[]> {
    const response = await fetch(`${API_BASE_URL}/properties/by_type/?type=${type}&page=${page}&page_size=${pageSize}`);
    if (!response.ok) {
      throw new Error('Failed to fetch properties');
    }
    const data = await response.json();
    return Array.isArray(data) ? data : data.results;
  }
};
