import React, { useState, useMemo, useEffect } from 'react';
import PropertyCard from '../components/PropertyCard';
import PropertyGallery from '../components/PropertyGallery';
import { Property, ListingStatus } from '../types';
import { propertyService } from '../services/propertyService';

const Properties: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'All' | ListingStatus>('All');
  const [selectedPropertyId, setSelectedPropertyId] = useState<string | number | null>(null);
  const [properties, setProperties] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProperties = async () => {
      try {
        setLoading(true);
        const data = await propertyService.getAllProperties();
        setProperties(data);
        setError(null);
      } catch (err) {
        setError('Failed to load properties');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchProperties();
  }, []);

  const filteredProperties = useMemo(() => {
    if (!properties) return [];
    if (activeTab === 'All') return properties;
    return properties.filter(p => p.status === activeTab);
  }, [activeTab, properties]);

  const selectedProperty = useMemo(() => 
    properties?.find(p => String(p.id) === String(selectedPropertyId)),
    [selectedPropertyId, properties]
  );

  return (
    <>
      {/* Page Header */}
      <header className="relative h-[40vh] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0">
          <img 
            src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=2000" 
            className="w-full h-full object-cover opacity-40"
            alt="Properties Header"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-[#050a14] via-[#050a14]/50 to-[#050a14]"></div>
        </div>
        
        <div className="relative z-10 text-center px-6">
          <h1 className="text-5xl md:text-7xl font-serif text-white mb-4 tracking-tight">
            Our <span className="italic text-[#d4af37]">Portfolio</span>
          </h1>
          <p className="text-xl text-slate-300 font-light">
            Discover exceptional properties across the globe
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow py-16 px-6 bg-[#050a14]">
        <div className="max-w-7xl mx-auto">
          
          {/* Filter Tabs */}
          <div className="flex flex-col md:flex-row justify-between items-center mb-12 gap-6">
            <div className="text-slate-400">
              Showing {filteredProperties.length} {filteredProperties.length === 1 ? 'property' : 'properties'}
            </div>
            
            <div className="flex bg-[#101827] p-1 rounded-sm border border-white/5">
              {(['All', ListingStatus.FOR_SALE, ListingStatus.FOR_RENT] as const).map((tab) => (
                <button
                  key={tab}
                  onClick={() => setActiveTab(tab)}
                  className={`px-8 py-2 text-sm uppercase tracking-widest transition-all ${
                    activeTab === tab 
                    ? 'bg-[#d4af37] text-[#050a14] font-bold' 
                    : 'text-slate-400 hover:text-white'
                  }`}
                >
                  {tab}
                </button>
              ))}
            </div>
          </div>

          {/* Properties Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {loading ? (
              <div className="col-span-full text-center py-20">
                <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#d4af37]"></div>
                <p className="text-slate-400 mt-4">Loading properties...</p>
              </div>
            ) : error ? (
              <div className="col-span-full text-center py-20">
                <p className="text-red-400">{error}</p>
              </div>
            ) : filteredProperties.length === 0 ? (
              <div className="col-span-full text-center py-20">
                <p className="text-slate-400">No properties found</p>
              </div>
            ) : (
              filteredProperties.map(property => (
                <PropertyCard 
                  key={property.id} 
                  property={property} 
                  onClick={(p) => setSelectedPropertyId(p.id)}
                />
              ))
            )}
          </div>
        </div>
      </main>

      {/* Modal - Property Details */}
      {selectedProperty && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-6 backdrop-blur-xl bg-[#050a14]/90 overflow-y-auto">
          <div className="bg-[#101827] max-w-6xl w-full rounded-2xl overflow-hidden border border-[#d4af37]/30 shadow-2xl relative animate-scaleIn">
            <button 
              onClick={() => setSelectedPropertyId(null)}
              className="absolute top-6 right-6 z-[110] p-2 bg-black/50 text-white rounded-full hover:bg-[#d4af37] transition-all"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>

            <div className="flex flex-col lg:flex-row h-full max-h-[90vh]">
              <div className="lg:w-3/5 h-[400px] lg:h-auto border-r border-white/5">
                <PropertyGallery images={selectedProperty.images} />
              </div>

              <div className="lg:w-2/5 p-8 lg:p-12 overflow-y-auto bg-[#101827]">
                <div className="text-[#d4af37] text-xs uppercase tracking-[0.3em] mb-4">
                  {selectedProperty.status} | {selectedProperty.type}
                </div>
                <h2 className="text-4xl font-serif text-white mb-4 leading-tight">{selectedProperty.title}</h2>
                <p className="text-2xl font-bold text-[#d4af37] mb-8">
                  {selectedProperty.price < 100000 
                    ? `${selectedProperty.price.toLocaleString()}/mo` 
                    : `${selectedProperty.price.toLocaleString()}`}
                </p>
                
                <div className="grid grid-cols-3 gap-4 mb-8 border-y border-white/10 py-6">
                  <div className="text-center">
                    <div className="text-white font-bold">{selectedProperty.beds}</div>
                    <div className="text-slate-500 text-[10px] uppercase tracking-wider">Bedrooms</div>
                  </div>
                  <div className="text-center">
                    <div className="text-white font-bold">{selectedProperty.baths}</div>
                    <div className="text-slate-500 text-[10px] uppercase tracking-wider">Bathrooms</div>
                  </div>
                  <div className="text-center">
                    <div className="text-white font-bold">{selectedProperty.sqft.toLocaleString()}</div>
                    <div className="text-slate-500 text-[10px] uppercase tracking-wider">Square Ft</div>
                  </div>
                </div>

                <div className="mb-8">
                  <h4 className="text-white font-bold mb-3 uppercase text-xs tracking-widest">Description</h4>
                  <p className="text-slate-400 leading-relaxed font-light">
                    {selectedProperty.description}
                  </p>
                </div>

                <div className="mb-12">
                  <h4 className="text-white font-bold mb-4 uppercase text-xs tracking-widest">Exquisite Amenities</h4>
                  <div className="flex flex-wrap gap-2">
                    {selectedProperty.amenities.map(item => (
                      <span key={item} className="bg-white/5 border border-white/10 px-3 py-1 rounded-sm text-xs text-slate-300">
                        {item}
                      </span>
                    ))}
                  </div>
                </div>

                <button className="w-full bg-[#d4af37] text-[#050a14] py-4 font-bold text-lg hover:bg-[#f1c40f] transition-all transform hover:scale-[1.02]">
                  Request Private Viewing
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Properties;
