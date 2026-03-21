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
        const data = await propertyService.getAllProperties();
        setProperties(data.slice(0, 3));
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchProperties();
  }, []);

  const selectedProperty = useMemo(() => 
    properties.find(p => String(p.id) === String(selectedPropertyId)),
    [selectedPropertyId, properties]
  );

  return (
    <>
      <section className="relative h-screen flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0">
          <div className="absolute inset-0 grid grid-cols-3 gap-1">
            <img src="https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&q=80&w=800" className="w-full h-full object-cover opacity-30" alt="Luxury Property 1" />
            <img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&q=80&w=800" className="w-full h-full object-cover opacity-30" alt="Luxury Property 2" />
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=800" className="w-full h-full object-cover opacity-30" alt="Luxury Property 3" />
          </div>
          <div className="absolute inset-0 bg-gradient-to-b from-[#050a14] via-[#050a14]/95 to-[#050a14]"></div>
        </div>
        
        <div className="relative z-10 text-center px-6 max-w-6xl">
          <div className="mb-8 inline-flex items-center gap-4 text-[#d4af37] text-xs uppercase tracking-[0.5em]">
            <div className="h-[1px] w-12 bg-[#d4af37]"></div>
            <span>Est. 2024</span>
            <div className="h-[1px] w-12 bg-[#d4af37]"></div>
          </div>
          
          <h1 className="text-7xl md:text-9xl font-serif text-white mb-6 tracking-tight leading-none">BELLEROCK</h1>
          <p className="text-2xl md:text-3xl text-[#d4af37] font-serif italic mb-8">Where Legacy Meets Luxury</p>
          <p className="text-lg text-slate-300 font-light max-w-3xl mx-auto mb-12 leading-relaxed">
            Curating the world's most distinguished properties for discerning clientele.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-6 justify-center items-center">
            <Link to="/properties" className="px-12 py-5 bg-[#d4af37] text-[#050a14] font-bold text-lg hover:bg-[#f1c40f] transition-all">
              Explore Portfolio
            </Link>
            <button className="px-12 py-5 border-2 border-white/30 text-white font-bold text-lg hover:bg-white/10 transition-all">
              Schedule Consultation
            </button>
          </div>
        </div>
      </section>

      <section className="py-32 px-6 bg-[#050a14]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-20">
            <h2 className="text-5xl md:text-6xl font-serif text-white mb-6">Featured <span className="italic text-[#d4af37]">Properties</span></h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
            {loading ? (
              <div className="col-span-full text-center py-20">
                <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#d4af37]"></div>
              </div>
            ) : (
              properties.map(property => (
                <PropertyCard key={property.id} property={property} onClick={(p) => setSelectedPropertyId(p.id)} />
              ))
            )}
          </div>
          <div className="text-center">
            <Link to="/properties" className="inline-block px-12 py-4 border-2 border-[#d4af37] text-[#d4af37] font-bold hover:bg-[#d4af37] hover:text-[#050a14] transition-all">
              View All Properties
            </Link>
          </div>
        </div>
      </section>

      {selectedProperty && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-6 backdrop-blur-xl bg-[#050a14]/90 overflow-y-auto">
          <div className="bg-[#101827] max-w-6xl w-full rounded-2xl overflow-hidden border border-[#d4af37]/30 shadow-2xl relative animate-scaleIn">
            <button onClick={() => setSelectedPropertyId(null)} className="absolute top-6 right-6 z-[110] p-2 bg-black/50 text-white rounded-full hover:bg-[#d4af37] transition-all">
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
            <div className="flex flex-col lg:flex-row h-full max-h-[90vh]">
              <div className="lg:w-3/5 h-[400px] lg:h-auto border-r border-white/5">
                <PropertyGallery images={selectedProperty.images} />
              </div>
              <div className="lg:w-2/5 p-8 lg:p-12 overflow-y-auto bg-[#101827]">
                <h2 className="text-4xl font-serif text-white mb-4">{selectedProperty.title}</h2>
                <p className="text-2xl font-bold text-[#d4af37] mb-8">${selectedProperty.price.toLocaleString()}</p>
                <p className="text-slate-400 mb-8">{selectedProperty.description}</p>
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
