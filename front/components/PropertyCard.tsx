
import React from 'react';
import { Property } from '../types';
import { COLORS } from '../constants';

interface PropertyCardProps {
  property: Property;
  onClick: (property: Property) => void;
}

const PropertyCard: React.FC<PropertyCardProps> = ({ property, onClick }) => {
  return (
    <div 
      className="group bg-[#101827] border border-white/5 rounded-lg overflow-hidden cursor-pointer transition-all duration-500 hover:border-[#d4af37]/50 hover:shadow-2xl hover:shadow-[#d4af37]/10"
      onClick={() => onClick(property)}
    >
      <div className="relative h-64 overflow-hidden">
        <img 
          src={property.images[0]} 
          alt={property.title}
          className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
          onError={(e) => {
            e.currentTarget.src = "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=1200";
          }}
        />
        <div className="absolute top-4 left-4 bg-[#050a14]/80 backdrop-blur-md px-3 py-1 text-[10px] uppercase tracking-widest text-[#d4af37] border border-[#d4af37]/30">
          {property.status}
        </div>
        <div className="absolute inset-0 bg-gradient-to-t from-[#050a14] via-transparent to-transparent opacity-60"></div>
      </div>
      
      <div className="p-6">
        <div className="flex justify-between items-start mb-2">
          <h3 className="text-xl font-serif text-white group-hover:text-[#d4af37] transition-colors">{property.title}</h3>
          <p className="text-[#d4af37] font-bold text-lg">
            {property.price < 100000 
              ? `$${property.price.toLocaleString()}/mo` 
              : `$${(property.price / 1000000).toFixed(1)}M`}
          </p>
        </div>
        <p className="text-slate-400 text-sm mb-4 flex items-center gap-1">
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          {property.location}
        </p>
        
        <div className="flex items-center gap-6 text-xs text-slate-400 border-t border-white/5 pt-4">
          <span className="flex items-center gap-2">
            <span className="text-white font-semibold">{property.beds}</span> Beds
          </span>
          <span className="flex items-center gap-2">
            <span className="text-white font-semibold">{property.baths}</span> Baths
          </span>
          <span className="flex items-center gap-2">
            <span className="text-white font-semibold">{property.sqft.toLocaleString()}</span> Sqft
          </span>
        </div>
      </div>
    </div>
  );
};

export default PropertyCard;
