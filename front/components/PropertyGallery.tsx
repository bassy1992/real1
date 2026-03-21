
import React, { useState } from 'react';

interface PropertyGalleryProps {
  images: string[];
}

const PropertyGallery: React.FC<PropertyGalleryProps> = ({ images }) => {
  const [activeIndex, setActiveIndex] = useState(0);

  return (
    <div className="flex flex-col h-full">
      {/* Main Image Viewer */}
      <div className="relative flex-grow overflow-hidden bg-black flex items-center justify-center">
        <img 
          src={images[activeIndex]} 
          alt={`View ${activeIndex + 1}`}
          className="max-w-full max-h-full object-contain transition-opacity duration-500"
          onError={(e) => {
            e.currentTarget.src = "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=1200";
          }}
        />
        
        {/* Navigation Arrows */}
        {images.length > 1 && (
          <>
            <button 
              onClick={() => setActiveIndex((prev) => (prev === 0 ? images.length - 1 : prev - 1))}
              className="absolute left-4 p-3 bg-black/40 text-white rounded-full hover:bg-[#d4af37] transition-all"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            <button 
              onClick={() => setActiveIndex((prev) => (prev === images.length - 1 ? 0 : prev + 1))}
              className="absolute right-4 p-3 bg-black/40 text-white rounded-full hover:bg-[#d4af37] transition-all"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </>
        )}
      </div>

      {/* Thumbnails */}
      <div className="p-4 bg-[#050a14] border-t border-white/10">
        <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-hide">
          {images.map((img, idx) => (
            <button
              key={idx}
              onClick={() => setActiveIndex(idx)}
              className={`relative flex-shrink-0 w-24 h-16 rounded-sm overflow-hidden border-2 transition-all ${
                activeIndex === idx ? 'border-[#d4af37]' : 'border-transparent opacity-50 hover:opacity-100'
              }`}
            >
              <img 
                src={img} 
                alt={`Thumb ${idx + 1}`} 
                className="w-full h-full object-cover"
                onError={(e) => {
                  e.currentTarget.src = "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=1200";
                }}
              />
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default PropertyGallery;
