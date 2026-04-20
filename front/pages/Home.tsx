import React, { useState, useMemo, useEffect } from 'react';
import { Link } from 'react-router-dom';
import PropertyCard from '../components/PropertyCard';
import PropertyGallery from '../components/PropertyGallery';
import { Property } from '../types';
import { propertyService } from '../services/propertyService';

const Home: React.FC = () => {
  const [selectedPropertyId, setSelectedPropertyId] = useState<string | number | null>(null);
  const [properties, setProperties] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProperties = async () => {
      try {
        setLoading(true);
        const response = await propertyService.getAllProperties();
        setProperties(response.results.slice(0, 3));
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchProperties();
  }, []);

  const selectedProperty = useMemo(() => 
    properties?.find(p => String(p.id) === String(selectedPropertyId)),
    [selectedPropertyId, properties]
  );

  return (
    <>
      {/* Hero Section - Full Screen */}
      <section className="relative h-screen flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0">
          <div className="absolute inset-0 grid grid-cols-3 gap-1">
            <img 
              src="https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&q=80&w=800" 
              className="w-full h-full object-cover opacity-30"
              alt="Luxury Property 1"
            />
            <img 
              src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&q=80&w=800" 
              className="w-full h-full object-cover opacity-30"
              alt="Luxury Property 2"
            />
            <img 
              src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=800" 
              className="w-full h-full object-cover opacity-30"
              alt="Luxury Property 3"
            />
          </div>
          <div className="absolute inset-0 bg-gradient-to-b from-[#050a14] via-[#050a14]/95 to-[#050a14]"></div>
        </div>

        
        <div className="relative z-10 text-center px-6 max-w-6xl">
          <div className="mb-8 inline-flex items-center gap-4 text-[#d4af37] text-xs uppercase tracking-[0.5em]">
            <div className="h-[1px] w-12 bg-[#d4af37]"></div>
            <span>Est. 2024</span>
            <div className="h-[1px] w-12 bg-[#d4af37]"></div>
          </div>
          
          <h1 className="text-7xl md:text-9xl font-serif text-white mb-6 tracking-tight leading-none">
            BELLROCK
          </h1>
          <p className="text-2xl md:text-3xl text-[#d4af37] font-serif italic mb-8">
            Where Legacy Meets Luxury
          </p>
          <p className="text-lg text-slate-300 font-light max-w-3xl mx-auto mb-12 leading-relaxed">
            Curating the world's most distinguished properties for discerning clientele. 
            From historic estates to modern masterpieces, we deliver unparalleled excellence.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-6 justify-center items-center">
            <Link 
              to="/properties"
              className="group relative px-12 py-5 bg-[#d4af37] text-[#050a14] font-bold text-lg overflow-hidden transition-all hover:shadow-2xl hover:shadow-[#d4af37]/50"
            >
              <span className="relative z-10">Explore Portfolio</span>
              <div className="absolute inset-0 bg-[#f1c40f] transform scale-x-0 group-hover:scale-x-100 transition-transform origin-left"></div>
            </Link>
            <button className="px-12 py-5 border-2 border-white/30 text-white font-bold text-lg hover:bg-white/10 hover:border-white/50 transition-all">
              Schedule Consultation
            </button>
          </div>

          <div className="mt-16 flex justify-center gap-16 text-center">
            <div>
              <div className="text-4xl font-serif text-[#d4af37] mb-2">50+</div>
              <div className="text-xs uppercase tracking-widest text-slate-400">Properties</div>
            </div>
            <div className="h-16 w-[1px] bg-white/20"></div>
            <div>
              <div className="text-4xl font-serif text-[#d4af37] mb-2">$2B+</div>
              <div className="text-xs uppercase tracking-widest text-slate-400">Portfolio Value</div>
            </div>
            <div className="h-16 w-[1px] bg-white/20"></div>
            <div>
              <div className="text-4xl font-serif text-[#d4af37] mb-2">15</div>
              <div className="text-xs uppercase tracking-widest text-slate-400">Countries</div>
            </div>
          </div>
        </div>

        <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
          <svg className="w-6 h-6 text-[#d4af37]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
          </svg>
        </div>
      </section>

      {/* About Section */}
      <section className="py-32 px-6 bg-gradient-to-b from-[#050a14] to-[#0a1120]">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
              <div className="text-[#d4af37] text-xs uppercase tracking-[0.4em] mb-6">Our Philosophy</div>
              <h2 className="text-5xl md:text-6xl font-serif text-white mb-8 leading-tight">
                Redefining <br />
                <span className="italic text-[#d4af37]">Luxury Living</span>
              </h2>
              <p className="text-slate-300 text-lg leading-relaxed mb-6">
                At Bellrock Holdings, we don't just sell properties—we curate lifestyles. 
                Each residence in our portfolio represents the pinnacle of architectural excellence, 
                prime location, and timeless elegance.
              </p>
              <p className="text-slate-400 leading-relaxed mb-8">
                Our dedicated team of experts provides white-glove service, ensuring every transaction 
                is seamless and every client's vision becomes reality. From acquisition to management, 
                we handle every detail with precision and discretion.
              </p>
              <Link 
                to="/properties"
                className="inline-flex items-center gap-3 text-[#d4af37] font-semibold hover:gap-5 transition-all"
              >
                Discover Our Story
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
                </svg>
              </Link>
            </div>
            
            <div className="relative">
              <div className="grid grid-cols-2 gap-4">
                <img 
                  src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=600" 
                  className="w-full h-64 object-cover rounded-sm"
                  alt="Luxury Interior"
                />
                <img 
                  src="https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&q=80&w=600" 
                  className="w-full h-64 object-cover rounded-sm mt-8"
                  alt="Luxury Exterior"
                />
              </div>
              <div className="absolute -bottom-8 -left-8 w-32 h-32 border-2 border-[#d4af37] rotate-45"></div>
            </div>
          </div>
        </div>
      </section>


      {/* Featured Properties */}
      <section className="py-32 px-6 bg-[#050a14]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-20">
            <div className="text-[#d4af37] text-xs uppercase tracking-[0.4em] mb-6">Exclusive Collection</div>
            <h2 className="text-5xl md:text-6xl font-serif text-white mb-6">
              Featured <span className="italic text-[#d4af37]">Properties</span>
            </h2>
            <p className="text-slate-400 text-lg max-w-2xl mx-auto">
              Handpicked selections from our most prestigious listings around the world
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
            {loading ? (
              <div className="col-span-full text-center py-20">
                <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#d4af37]"></div>
                <p className="text-slate-400 mt-4">Loading properties...</p>
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

          <div className="text-center">
            <Link 
              to="/properties"
              className="inline-block px-12 py-4 border-2 border-[#d4af37] text-[#d4af37] font-bold hover:bg-[#d4af37] hover:text-[#050a14] transition-all"
            >
              View Complete Portfolio
            </Link>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="py-32 px-6 bg-gradient-to-b from-[#050a14] to-[#0a1120]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-20">
            <div className="text-[#d4af37] text-xs uppercase tracking-[0.4em] mb-6">What We Offer</div>
            <h2 className="text-5xl md:text-6xl font-serif text-white mb-6">
              Comprehensive <span className="italic text-[#d4af37]">Services</span>
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="group p-10 bg-[#101827] border border-white/5 hover:border-[#d4af37]/50 transition-all">
              <div className="w-16 h-16 border-2 border-[#d4af37] flex items-center justify-center mb-6 group-hover:rotate-45 transition-transform">
                <svg className="w-8 h-8 text-[#d4af37] group-hover:-rotate-45 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                </svg>
              </div>
              <h3 className="text-2xl font-serif text-white mb-4">Property Sales</h3>
              <p className="text-slate-400 leading-relaxed">
                Expert guidance through every step of acquiring your dream property, from initial search to final closing.
              </p>
            </div>

            <div className="group p-10 bg-[#101827] border border-white/5 hover:border-[#d4af37]/50 transition-all">
              <div className="w-16 h-16 border-2 border-[#d4af37] flex items-center justify-center mb-6 group-hover:rotate-45 transition-transform">
                <svg className="w-8 h-8 text-[#d4af37] group-hover:-rotate-45 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />
                </svg>
              </div>
              <h3 className="text-2xl font-serif text-white mb-4">Luxury Rentals</h3>
              <p className="text-slate-400 leading-relaxed">
                Premium rental properties with full concierge services, perfect for extended stays or investment opportunities.
              </p>
            </div>

            <div className="group p-10 bg-[#101827] border border-white/5 hover:border-[#d4af37]/50 transition-all">
              <div className="w-16 h-16 border-2 border-[#d4af37] flex items-center justify-center mb-6 group-hover:rotate-45 transition-transform">
                <svg className="w-8 h-8 text-[#d4af37] group-hover:-rotate-45 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </div>
              <h3 className="text-2xl font-serif text-white mb-4">Estate Management</h3>
              <p className="text-slate-400 leading-relaxed">
                Comprehensive property management services ensuring your investment maintains its value and prestige.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-32 px-6 bg-[#050a14] relative overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <img 
            src="https://images.unsplash.com/photo-1600607687644-c7171b42398b?auto=format&fit=crop&q=80&w=2000" 
            className="w-full h-full object-cover"
            alt="Background"
          />
        </div>
        <div className="relative z-10 max-w-4xl mx-auto text-center">
          <h2 className="text-5xl md:text-6xl font-serif text-white mb-8">
            Ready to Find Your <br />
            <span className="italic text-[#d4af37]">Perfect Property?</span>
          </h2>
          <p className="text-xl text-slate-300 mb-12 leading-relaxed">
            Let our experts guide you to the residence of your dreams. 
            Schedule a private consultation today.
          </p>
          <div className="flex flex-col sm:flex-row gap-6 justify-center">
            <button className="px-12 py-5 bg-[#d4af37] text-[#050a14] font-bold text-lg hover:bg-[#f1c40f] transition-all">
              Contact Our Team
            </button>
            <Link 
              to="/properties"
              className="px-12 py-5 border-2 border-white/30 text-white font-bold text-lg hover:bg-white/10 transition-all"
            >
              Browse Properties
            </Link>
          </div>
        </div>
      </section>


      {/* Property Modal */}
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
                    ? `$${selectedProperty.price.toLocaleString()}/mo` 
                    : `$${selectedProperty.price.toLocaleString()}`}
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
                  <h4 className="text-white font-bold mb-4 uppercase text-xs tracking-widest">Amenities</h4>
                  <div className="flex flex-wrap gap-2">
                    {selectedProperty.amenities.map(item => (
                      <span key={item} className="bg-white/5 border border-white/10 px-3 py-1 rounded-sm text-xs text-slate-300">
                        {item}
                      </span>
                    ))}
                  </div>
                </div>

                <button className="w-full bg-[#d4af37] text-[#050a14] py-4 font-bold text-lg hover:bg-[#f1c40f] transition-all">
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

export default Home;
