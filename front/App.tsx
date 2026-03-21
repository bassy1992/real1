import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Properties from './pages/Properties';
import Rentals from './pages/Rentals';
import Investments from './pages/Investments';

const App: React.FC = () => {
  return (
    <Router>
      <div className="min-h-screen bg-[#050a14] flex flex-col">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/properties" element={<Properties />} />
          <Route path="/rentals" element={<Rentals />} />
          <Route path="/investments" element={<Investments />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
