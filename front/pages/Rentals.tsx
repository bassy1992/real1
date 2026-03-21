import React, { useState, useMemo, useEffect } from 'react';
import PropertyCard from '../components/PropertyCard';
import PropertyGallery from '../components/PropertyGallery';
import { Property, ListingStatus } from '../types';
import { propertyService } from '../services/propertyService';

const Rentals: React.FC = () => {
  const [selectedPropertyId, setSelectedPropertyId] = useState<string | number | null>(null);
  const [properties, setProperties] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchRentals = async () => {
      try {
        setLoading(true);
        const data = await propertyService.getPropertiesByStatus(ListingStatus.FOR_RENT);
        setProperties(data);
        setError(null);
      } catch (err) {
        setError('Failed to load rental properties');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchRentals();
  }, []);

  const selectedProperty = useMemo(() => 
    properties.find(p => String(p.id) === String(selectedPropertyId)),
    [selectedPropertyId, properties]
  );

  return (
    <>
      <header className="relative h-[50vh] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0">
          <img 
            src="https://images.unsplash.com/photo-1600566753190-17f0bb2a6c3e?auto=format&fit=crop&q=80&w=2000" 
            className="w-full h-full object-cover opacity-40"
            alt="Luxury Rentals"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-[#050a14] via-[#050a14]/50 to-[#050a14]"></div>
        </div>
        
        <div className="relative z-10 text-center px-6 max-w-4xl">
          <div className="mb-6 inline-flex items-center gap-4 text-[#d4af37] text-xs uppercase tracking-[0.5em]">
            <div className="h-[1px] w-12 bg-[#d4af37]"></div>
            <span>Premium Rentals</span>
            <div className="h-[1px] w-12 bg-[#d4af37]"></div>
          </div>
          <h1 className="text-6xl md:text-8xl font-serif text-white mb-6 tracking-tight leading-none">
            Luxury <span className="italic text-[#d4af37]">Rentals</span>
          </h1>
          <p className="text-xl text-slate-300 font-light leading-relaxed">
            Experience world-class living with our curated collection of premium rental properties
          </p>
        </div>
      </header>

      <main className="py-20 px-6 bg-[#050a14]">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-center mb-12 gap-6">
            <div>
              <h2 className="text-3xl font-serif text-white mb-2">Available Rentals</h2>
              <p className="text-slate-400">
                {loading ? 'Loading...' : `${properties.length} ${properties.length === 1 ? 'property' : 'properties'} available`}
              </p>
            </div>
            
            <div className="flex items-center gap-4 text-sm text-slate-400">
              <svg className="w-5 h-5 text-[#d4af37]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>All properties include full concierge services</span>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {loading ? (
              <div className="col-span-full text-center py-20">
                <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#d4af37]"></div>
                <p className="text-slate-400 mt-4">Loading rental properties...</p>
              </div>
            ) : error ? (
              <div className="col-span-full text-center py-20">
                <p className="text-red-400">{error}</p>
              </div>
            ) : properties.length === 0 ? (
              <div className="col-span-full text-center py-20">
                <svg className="w-16 h-16 text-slate-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                </svg>
                <p className="text-slate-400 text-lg">No rental properties available at the moment</p>
                <p className="text-slate-500 text-sm mt-2">Please check back soon or contact us for upcoming listings</p>
              </div>
            ) : (
              properties.map(property => (
                <PropertyCard 
                  key={property.id} 
                  property={property} 
                  onClick={(p) => setSelectedPropertyId(p.id)}
                />
              ))
            )}
          </div>

          {!loading && properties.length > 0 && (
            <div className="mt-16 p-10 bg-gradient-to-r from-[#101827] to-[#0a1120] border border-white/5 rounded-lg">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
                <div>
                  <div className="w-16 h-16 border-2 border-[#d4af37] flex items-center justify-center mx-auto mb-4 rotate-45">
                    <svg className="w-8 h-8 text-[#d4af37] -rotate-45" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <h3 className="text-xl font-serif text-white mb-2">Flexible Terms</h3>
                  <p className="text-slate-400 text-sm">Short-term and long-term rental options available</p>
                </div>
                <div>
                  <div className="w-16 h-16 border-2 border-[#d4af37] flex items-center justify-center mx-auto mb-4 rotate-45">
                    <svg className="w-8 h-8 text-[#d4af37] -rotate-45" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                    </svg>
                  </div>
                  <h3 className="text-xl font-serif text-white mb-2">Concierge Service</h3>
                  <p className="text-slate-400 text-sm">24/7 dedicated support for all your needs</p>
                </div>
                <div>
                  <div className="w-16 h-16 border-2 border-[#d4af37] flex items-center justify-center mx-auto mb-4 rotate-45">
                    <svg className="w-8 h-8 text-[#d4af37] -rotate-45" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                    </svg>
                  </div>
                  <h3 className="text-xl font-serif text-white mb-2">Fully Furnished</h3>
                  <p className="text-slate-400 text-sm">Move-in ready with premium furnishings</p>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>

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
                <p className="text-3xl font-bold text-[#d4af37] mb-2">
                  ${selectedProperty.price.toLocaleString()}<span className="text-lg text-slate-400">/month</span>
                </p>
                <p className="text-sm text-slate-500 mb-8">Utilities and concierge services included</p>
                
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

                <div className="mb-8">
                  <h4 className="text-white font-bold mb-4 uppercase text-xs tracking-widest">Amenities</h4>
                  <div className="flex flex-wrap gap-2">
                    {selectedProperty.amenities.map(item => (
                      <span key={item} className="bg-white/5 border border-white/10 px-3 py-1 rounded-sm text-xs text-slate-300">
                        {item}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="mb-8 p-4 bg-[#d4af37]/10 border border-[#d4af37]/30 rounded">
                  <h4 className="text-[#d4af37] font-bold mb-2 text-sm">Rental Terms</h4>
                  <ul className="text-slate-400 text-sm space-y-1">
                    <li>• Minimum 6-month lease</li>
                    <li>• First and last month required</li>
                    <li>• Security deposit: 1 month rent</li>
                    <li>• Pets negotiable with deposit</li>
                  </ul>
                </div>

                <button className="w-full bg-[#d4af37] text-[#050a14] py-4 font-bold text-lg hover:bg-[#f1c40f] transition-all">
                  Schedule Viewing
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Rentals;
