import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-[#050a14] border-t border-white/5 pt-24 pb-12 px-6">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-16 mb-24">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center gap-4 mb-8">
              <div className="w-12 h-12 border-2 border-[#d4af37] flex items-center justify-center rotate-45">
                <div className="w-8 h-8 bg-[#d4af37] -rotate-45"></div>
              </div>
              <div className="flex flex-col">
                <span className="text-2xl font-serif font-bold tracking-widest text-white leading-none">BELLROCK</span>
                <span className="text-xs tracking-[0.4em] text-[#d4af37]">HOLDINGS LIMITED</span>
              </div>
            </div>
            <p className="text-slate-400 max-w-md leading-loose">
              Setting the global standard for luxury real estate services. We specialize in the acquisition, management, and rental of prestigious properties across the world's most desirable locations.
            </p>
          </div>
          
          <div>
            <h4 className="text-white font-serif text-xl mb-6">Experience</h4>
            <ul className="space-y-4 text-slate-400 text-sm">
              <li><a href="#" className="hover:text-[#d4af37] transition-colors">Residential Sales</a></li>
              <li><a href="#" className="hover:text-[#d4af37] transition-colors">Luxury Rentals</a></li>
              <li><a href="#" className="hover:text-[#d4af37] transition-colors">Estate Management</a></li>
              <li><a href="#" className="hover:text-[#d4af37] transition-colors">Private Advisory</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-white font-serif text-xl mb-6">Contact</h4>
            <ul className="space-y-4 text-slate-400 text-sm">
              <li>21 Sowutuom, Evans Kwao Street</li>
              <li>Accra, Ghana</li>
              <li>Post Address: GC-088-3111</li>
              <li className="text-[#d4af37]">concierge@bellrock.com</li>
            </ul>
          </div>
        </div>
        
        <div className="pt-12 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-8 text-[10px] tracking-[0.2em] uppercase text-slate-500">
          <p>© 2024 Bellrock Holdings Limited. All Rights Reserved.</p>
          <div className="flex gap-12">
            <a href="#" className="hover:text-white">Privacy Policy</a>
            <a href="#" className="hover:text-white">Terms of Service</a>
            <a href="#" className="hover:text-white">Cookies</a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
