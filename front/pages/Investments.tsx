import React, { useState, useEffect } from 'react';
import { InvestmentOpportunity, investmentService } from '../services/investmentService';
import PropertyGallery from '../components/PropertyGallery';

const Investments: React.FC = () => {
  const [opportunities, setOpportunities] = useState<InvestmentOpportunity[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedOpportunity, setSelectedOpportunity] = useState<InvestmentOpportunity | null>(null);
  const [filterType, setFilterType] = useState<string>('All');
  const [filterRisk, setFilterRisk] = useState<string>('All');

  useEffect(() => {
    fetchOpportunities();
  }, []);

  const fetchOpportunities = async () => {
    try {
      setLoading(true);
      const data = await investmentService.getAllOpportunities();
      setOpportunities(data);
    } catch (error) {
      console.error('Error fetching opportunities:', error);
    } finally {
      setLoading(false);
    }
  };

  const filteredOpportunities = opportunities.filter(opp => {
    const typeMatch = filterType === 'All' || opp.investment_type === filterType;
    const riskMatch = filterRisk === 'All' || opp.risk_level === filterRisk;
    return typeMatch && riskMatch;
  });

  const getRiskColor = (risk: string) => {
    switch (risk) {
      case 'Low': return 'text-green-400 bg-green-400/10 border-green-400/30';
      case 'Medium': return 'text-yellow-400 bg-yellow-400/10 border-yellow-400/30';
      case 'High': return 'text-red-400 bg-red-400/10 border-red-400/30';
      default: return 'text-gray-400 bg-gray-400/10 border-gray-400/30';
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'Active': return 'text-emerald-400 bg-emerald-400/10 border-emerald-400/30';
      case 'Funded': return 'text-blue-400 bg-blue-400/10 border-blue-400/30';
      case 'Coming Soon': return 'text-purple-400 bg-purple-400/10 border-purple-400/30';
      default: return 'text-gray-400 bg-gray-400/10 border-gray-400/30';
    }
  };

  return (
    <div className="min-h-screen bg-[#050a14] pt-24 pb-20">
      {/* Hero Section */}
      <section className="relative py-20 px-6 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-b from-[#d4af37]/5 to-transparent"></div>
        <div className="max-w-7xl mx-auto relative z-10">
          <div className="text-center mb-12">
            <div className="inline-flex items-center gap-4 text-[#d4af37] text-xs uppercase tracking-[0.5em] mb-6">
              <div className="h-[1px] w-12 bg-[#d4af37]"></div>
              <span>Investment Opportunities</span>
              <div className="h-[1px] w-12 bg-[#d4af37]"></div>
            </div>
            <h1 className="text-6xl md:text-7xl font-serif text-white mb-6">
              Build Your <span className="italic text-[#d4af37]">Legacy</span>
            </h1>
            <p className="text-xl text-slate-300 max-w-3xl mx-auto leading-relaxed">
              Exclusive access to curated real estate investment opportunities with institutional-grade returns
            </p>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-5xl mx-auto">
            <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-lg p-6 text-center">
              <div className="text-3xl font-bold text-[#d4af37] mb-2">$68M+</div>
              <div className="text-sm text-slate-400">Total Investment Volume</div>
            </div>
            <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-lg p-6 text-center">
              <div className="text-3xl font-bold text-[#d4af37] mb-2">12.5%</div>
              <div className="text-sm text-slate-400">Avg. Annual Return</div>
            </div>
            <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-lg p-6 text-center">
              <div className="text-3xl font-bold text-[#d4af37] mb-2">4</div>
              <div className="text-sm text-slate-400">Active Opportunities</div>
            </div>
            <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-lg p-6 text-center">
              <div className="text-3xl font-bold text-[#d4af37] mb-2">850+</div>
              <div className="text-sm text-slate-400">Satisfied Investors</div>
            </div>
          </div>
        </div>
      </section>

      {/* Filters */}
      <section className="px-6 mb-12">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-wrap gap-4 justify-center">
            <div className="flex gap-2">
              <button
                onClick={() => setFilterType('All')}
                className={`px-6 py-3 rounded-lg font-medium transition-all ${
                  filterType === 'All'
                    ? 'bg-[#d4af37] text-[#050a14]'
                    : 'bg-white/5 text-slate-300 hover:bg-white/10'
                }`}
              >
                All Types
              </button>
              {['Fractional', 'Full', 'Development', 'REIT'].map(type => (
                <button
                  key={type}
                  onClick={() => setFilterType(type)}
                  className={`px-6 py-3 rounded-lg font-medium transition-all ${
                    filterType === type
                      ? 'bg-[#d4af37] text-[#050a14]'
                      : 'bg-white/5 text-slate-300 hover:bg-white/10'
                  }`}
                >
                  {type}
                </button>
              ))}
            </div>
            <div className="flex gap-2">
              {['All', 'Low', 'Medium', 'High'].map(risk => (
                <button
                  key={risk}
                  onClick={() => setFilterRisk(risk)}
                  className={`px-6 py-3 rounded-lg font-medium transition-all ${
                    filterRisk === risk
                      ? 'bg-[#d4af37] text-[#050a14]'
                      : 'bg-white/5 text-slate-300 hover:bg-white/10'
                  }`}
                >
                  {risk} Risk
                </button>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Opportunities Grid */}
      <section className="px-6">
        <div className="max-w-7xl mx-auto">
          {loading ? (
            <div className="text-center py-20">
              <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#d4af37]"></div>
            </div>
          ) : (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              {filteredOpportunities.map(opp => (
                <div
                  key={opp.id}
                  onClick={() => setSelectedOpportunity(opp)}
                  className="group bg-gradient-to-br from-white/5 to-white/[0.02] backdrop-blur-sm border border-white/10 rounded-2xl overflow-hidden hover:border-[#d4af37]/50 transition-all cursor-pointer"
                >
                  {/* Property Image */}
                  <div className="relative h-64 overflow-hidden">
                    <img
                      src={opp.property_details?.images?.[0] || 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c'}
                      alt={opp.title}
                      className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-[#050a14] via-[#050a14]/50 to-transparent"></div>
                    <div className="absolute top-4 right-4 flex gap-2">
                      <span className={`px-3 py-1 rounded-full text-xs font-bold border ${getStatusColor(opp.status)}`}>
                        {opp.status}
                      </span>
                      <span className={`px-3 py-1 rounded-full text-xs font-bold border ${getRiskColor(opp.risk_level)}`}>
                        {opp.risk_level} Risk
                      </span>
                    </div>
                  </div>

                  {/* Content */}
                  <div className="p-6">
                    <div className="flex items-center gap-2 text-[#d4af37] text-sm mb-3">
                      <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M8.433 7.418c.155-.103.346-.196.567-.267v1.698a2.305 2.305 0 01-.567-.267C8.07 8.34 8 8.114 8 8c0-.114.07-.34.433-.582zM11 12.849v-1.698c.22.071.412.164.567.267.364.243.433.468.433.582 0 .114-.07.34-.433.582a2.305 2.305 0 01-.567.267z" />
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-13a1 1 0 10-2 0v.092a4.535 4.535 0 00-1.676.662C6.602 6.234 6 7.009 6 8c0 .99.602 1.765 1.324 2.246.48.32 1.054.545 1.676.662v1.941c-.391-.127-.68-.317-.843-.504a1 1 0 10-1.51 1.31c.562.649 1.413 1.076 2.353 1.253V15a1 1 0 102 0v-.092a4.535 4.535 0 001.676-.662C13.398 13.766 14 12.991 14 12c0-.99-.602-1.765-1.324-2.246A4.535 4.535 0 0011 9.092V7.151c.391.127.68.317.843.504a1 1 0 101.511-1.31c-.563-.649-1.413-1.076-2.354-1.253V5z" clipRule="evenodd" />
                      </svg>
                      <span className="font-semibold">{opp.investment_type}</span>
                    </div>

                    <h3 className="text-2xl font-serif text-white mb-3 group-hover:text-[#d4af37] transition-colors">
                      {opp.title}
                    </h3>

                    <p className="text-slate-400 text-sm mb-6 line-clamp-2">
                      {opp.description}
                    </p>

                    {/* Funding Progress */}
                    <div className="mb-6">
                      <div className="flex justify-between text-sm mb-2">
                        <span className="text-slate-400">Funding Progress</span>
                        <span className="text-[#d4af37] font-bold">{opp.funding_percentage.toFixed(1)}%</span>
                      </div>
                      <div className="h-2 bg-white/10 rounded-full overflow-hidden">
                        <div
                          className="h-full bg-gradient-to-r from-[#d4af37] to-[#f1c40f] transition-all"
                          style={{ width: `${Math.min(opp.funding_percentage, 100)}%` }}
                        ></div>
                      </div>
                    </div>

                    {/* Key Metrics */}
                    <div className="grid grid-cols-3 gap-4 mb-6">
                      <div>
                        <div className="text-xs text-slate-500 mb-1">Min. Investment</div>
                        <div className="text-white font-bold">
                          ${parseFloat(opp.minimum_investment).toLocaleString(undefined, { maximumFractionDigits: 0 })}
                        </div>
                      </div>
                      <div>
                        <div className="text-xs text-slate-500 mb-1">Annual Return</div>
                        <div className="text-emerald-400 font-bold">{opp.projected_annual_return}%</div>
                      </div>
                      <div>
                        <div className="text-xs text-slate-500 mb-1">Term</div>
                        <div className="text-white font-bold">{Math.floor(opp.investment_term_months / 12)}y</div>
                      </div>
                    </div>

                    <button className="w-full py-3 bg-[#d4af37]/10 border border-[#d4af37] text-[#d4af37] font-bold rounded-lg hover:bg-[#d4af37] hover:text-[#050a14] transition-all">
                      View Details
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>


      {/* Detail Modal */}
      {selectedOpportunity && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-6 backdrop-blur-xl bg-[#050a14]/95 overflow-y-auto">
          <div className="bg-[#0a1628] max-w-6xl w-full rounded-2xl overflow-hidden border border-[#d4af37]/30 shadow-2xl relative">
            <button
              onClick={() => setSelectedOpportunity(null)}
              className="absolute top-6 right-6 z-10 p-2 bg-black/50 text-white rounded-full hover:bg-[#d4af37] transition-all"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>

            <div className="grid lg:grid-cols-2 gap-0">
              {/* Left: Images */}
              <div className="h-[400px] lg:h-auto">
                <PropertyGallery images={selectedOpportunity.property_details?.images || []} />
              </div>

              {/* Right: Details */}
              <div className="p-8 lg:p-12 overflow-y-auto max-h-[90vh]">
                <div className="flex gap-2 mb-4">
                  <span className={`px-3 py-1 rounded-full text-xs font-bold border ${getStatusColor(selectedOpportunity.status)}`}>
                    {selectedOpportunity.status}
                  </span>
                  <span className={`px-3 py-1 rounded-full text-xs font-bold border ${getRiskColor(selectedOpportunity.risk_level)}`}>
                    {selectedOpportunity.risk_level} Risk
                  </span>
                  <span className="px-3 py-1 rounded-full text-xs font-bold border border-[#d4af37] text-[#d4af37]">
                    {selectedOpportunity.investment_type}
                  </span>
                </div>

                <h2 className="text-4xl font-serif text-white mb-4">{selectedOpportunity.title}</h2>
                <p className="text-slate-400 mb-8">{selectedOpportunity.description}</p>

                {/* Investment Details */}
                <div className="bg-white/5 rounded-xl p-6 mb-8">
                  <h3 className="text-xl font-serif text-white mb-4">Investment Overview</h3>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <div className="text-sm text-slate-500 mb-1">Total Needed</div>
                      <div className="text-2xl font-bold text-white">
                        ${parseFloat(selectedOpportunity.total_investment_needed).toLocaleString()}
                      </div>
                    </div>
                    <div>
                      <div className="text-sm text-slate-500 mb-1">Current Funding</div>
                      <div className="text-2xl font-bold text-[#d4af37]">
                        ${parseFloat(selectedOpportunity.current_funding).toLocaleString()}
                      </div>
                    </div>
                    <div>
                      <div className="text-sm text-slate-500 mb-1">Minimum Investment</div>
                      <div className="text-xl font-bold text-white">
                        ${parseFloat(selectedOpportunity.minimum_investment).toLocaleString()}
                      </div>
                    </div>
                    <div>
                      <div className="text-sm text-slate-500 mb-1">Remaining</div>
                      <div className="text-xl font-bold text-emerald-400">
                        ${parseFloat(selectedOpportunity.remaining_investment).toLocaleString()}
                      </div>
                    </div>
                  </div>

                  <div className="mt-4">
                    <div className="h-3 bg-white/10 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-[#d4af37] to-[#f1c40f]"
                        style={{ width: `${Math.min(selectedOpportunity.funding_percentage, 100)}%` }}
                      ></div>
                    </div>
                    <div className="text-center mt-2 text-[#d4af37] font-bold">
                      {selectedOpportunity.funding_percentage.toFixed(1)}% Funded
                    </div>
                  </div>
                </div>

                {/* Returns */}
                <div className="bg-gradient-to-br from-emerald-500/10 to-emerald-500/5 border border-emerald-500/20 rounded-xl p-6 mb-8">
                  <h3 className="text-xl font-serif text-white mb-4">Projected Returns</h3>
                  <div className="grid grid-cols-2 gap-6">
                    <div>
                      <div className="text-sm text-slate-400 mb-2">Annual Return</div>
                      <div className="text-3xl font-bold text-emerald-400">
                        {selectedOpportunity.projected_annual_return}%
                      </div>
                    </div>
                    <div>
                      <div className="text-sm text-slate-400 mb-2">Appreciation</div>
                      <div className="text-3xl font-bold text-emerald-400">
                        {selectedOpportunity.projected_appreciation}%
                      </div>
                    </div>
                  </div>
                  <div className="mt-4 pt-4 border-t border-emerald-500/20">
                    <div className="text-sm text-slate-400">Investment Term</div>
                    <div className="text-xl font-bold text-white">
                      {Math.floor(selectedOpportunity.investment_term_months / 12)} Years ({selectedOpportunity.investment_term_months} months)
                    </div>
                  </div>
                </div>

                {/* Highlights */}
                {selectedOpportunity.highlights.length > 0 && (
                  <div className="mb-8">
                    <h3 className="text-xl font-serif text-white mb-4">Key Highlights</h3>
                    <ul className="space-y-3">
                      {selectedOpportunity.highlights.map((highlight, idx) => (
                        <li key={idx} className="flex items-start gap-3 text-slate-300">
                          <svg className="w-5 h-5 text-[#d4af37] mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                          </svg>
                          <span>{highlight}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* CTA */}
                <div className="flex gap-4">
                  <button className="flex-1 py-4 bg-[#d4af37] text-[#050a14] font-bold text-lg rounded-lg hover:bg-[#f1c40f] transition-all">
                    Express Interest
                  </button>
                  <button className="px-6 py-4 border-2 border-white/30 text-white font-bold rounded-lg hover:bg-white/10 transition-all">
                    Download Prospectus
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Investments;
