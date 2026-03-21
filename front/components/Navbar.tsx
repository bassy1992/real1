
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { COLORS } from '../constants';

const Navbar: React.FC = () => {
  const navigate = useNavigate();

  return (
    <nav className="sticky top-0 z-50 bg-[#050a14]/90 backdrop-blur-md border-b border-white/10 px-6 py-4">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <Link to="/" className="flex items-center gap-4 cursor-pointer">
          <div className="w-10 h-10 border-2 border-[#d4af37] flex items-center justify-center rotate-45">
            <div className="w-6 h-6 bg-[#d4af37] -rotate-45"></div>
          </div>
          <div className="flex flex-col">
            <span className="text-xl font-serif font-bold tracking-widest text-white leading-none">BELLEROCK</span>
            <span className="text-[10px] tracking-[0.3em] text-[#d4af37]">HOLDINGS LIMITED</span>
          </div>
        </Link>
        
        <div className="hidden md:flex items-center gap-8 text-sm font-medium tracking-wider uppercase text-slate-300">
          <Link to="/" className="hover:text-[#d4af37] transition-colors">Home</Link>
          <Link to="/properties" className="hover:text-[#d4af37] transition-colors">Properties</Link>
          <Link to="/rentals" className="hover:text-[#d4af37] transition-colors">Rentals</Link>
          <Link to="/investments" className="hover:text-[#d4af37] transition-colors">Investments</Link>
          <button className="bg-[#d4af37] text-[#050a14] px-6 py-2 rounded-sm font-bold hover:bg-[#f1c40f] transition-all">
            Contact Us
          </button>
        </div>

        <button className="md:hidden text-[#d4af37]">
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16m-7 6h7" />
          </svg>
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
