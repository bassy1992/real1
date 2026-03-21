
import React, { useState } from 'react';
import { analyzePropertyQuery } from '../services/geminiService';
import { Property } from '../types';

interface AIAssistantProps {
  onSuggest: (propertyId: string | number) => void;
  properties: Property[];
}

const AIAssistant: React.FC<AIAssistantProps> = ({ onSuggest, properties }) => {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState<any>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    try {
      const result = await analyzePropertyQuery(query, properties);
      setResponse(result);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-[#101827] border border-[#d4af37]/20 p-8 rounded-xl max-w-4xl mx-auto shadow-2xl">
      <div className="flex items-center gap-4 mb-6">
        <div className="w-12 h-12 rounded-full bg-gradient-to-br from-[#d4af37] to-[#f1c40f] flex items-center justify-center">
          <svg className="w-6 h-6 text-[#050a14]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
        </div>
        <div>
          <h2 className="text-2xl font-serif text-white">Bellerock AI Concierge</h2>
          <p className="text-slate-400 text-sm">Tell me your dream lifestyle, and I'll find the perfect match.</p>
        </div>
      </div>

      <form onSubmit={handleSearch} className="relative mb-6">
        <input 
          type="text" 
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Example: I'm looking for a modern beach house with a private pool in Malibu under $15M..."
          className="w-full bg-[#050a14] border border-white/10 rounded-lg py-4 px-6 text-white placeholder-slate-500 focus:outline-none focus:border-[#d4af37] transition-all"
        />
        <button 
          disabled={loading}
          className="absolute right-2 top-2 bottom-2 bg-[#d4af37] text-[#050a14] px-6 rounded-md font-bold hover:bg-[#f1c40f] disabled:opacity-50 transition-all"
        >
          {loading ? 'Analyzing...' : 'Ask AI'}
        </button>
      </form>

      {response && (
        <div className="space-y-6 animate-fadeIn">
          <div className="p-4 bg-white/5 rounded-lg border-l-4 border-[#d4af37]">
            <p className="text-slate-300 italic">"{response.generalAdvice}"</p>
          </div>
          
          <div className="grid md:grid-cols-2 gap-4">
            {response.suggestions.map((s: any, idx: number) => {
              const prop = MOCK_PROPERTIES.find(p => p.id === s.propertyId);
              if (!prop) return null;
              return (
                <div 
                  key={idx}
                  onClick={() => onSuggest(prop.id)}
                  className="bg-[#050a14] p-4 rounded-lg border border-white/5 cursor-pointer hover:border-[#d4af37]/30 transition-all"
                >
                  <h4 className="text-[#d4af37] font-semibold mb-1">{prop.title}</h4>
                  <p className="text-xs text-slate-400 line-clamp-2">{s.reasoning}</p>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};

export default AIAssistant;
