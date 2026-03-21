import { API_BASE_URL } from '../constants';

export interface InvestmentOpportunity {
  id: number;
  property_ref: number;
  property_details: any;
  title: string;
  investment_type: 'Fractional' | 'Full' | 'Development' | 'REIT';
  status: 'Active' | 'Funded' | 'Closed' | 'Coming Soon';
  risk_level: 'Low' | 'Medium' | 'High';
  total_investment_needed: string;
  minimum_investment: string;
  current_funding: string;
  funding_percentage: number;
  remaining_investment: string;
  projected_annual_return: string;
  projected_appreciation: string;
  investment_term_months: number;
  description: string;
  highlights: string[];
  financial_projections: any;
  documents: string[];
  start_date: string;
  end_date: string;
}

class InvestmentService {
  async getAllOpportunities(): Promise<InvestmentOpportunity[]> {
    const response = await fetch(`${API_BASE_URL}/investments/opportunities/`);
    if (!response.ok) throw new Error('Failed to fetch investment opportunities');
    return response.json();
  }

  async getActiveOpportunities(): Promise<InvestmentOpportunity[]> {
    const response = await fetch(`${API_BASE_URL}/investments/opportunities/active/`);
    if (!response.ok) throw new Error('Failed to fetch active opportunities');
    return response.json();
  }

  async getOpportunityById(id: number): Promise<InvestmentOpportunity> {
    const response = await fetch(`${API_BASE_URL}/investments/opportunities/${id}/`);
    if (!response.ok) throw new Error('Failed to fetch opportunity');
    return response.json();
  }

  async getOpportunitiesByType(type: string): Promise<InvestmentOpportunity[]> {
    const response = await fetch(`${API_BASE_URL}/investments/opportunities/by_type/?type=${type}`);
    if (!response.ok) throw new Error('Failed to fetch opportunities by type');
    return response.json();
  }
}

export const investmentService = new InvestmentService();
