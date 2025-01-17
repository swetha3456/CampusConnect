import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import Login from './components/Login';
import Register from './components/Register';
import HomePage from './components/HomePage';
import PeerTutor from './pages/PeerTutor';
const App = () => {
  return (
    <div>
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/home" element={<HomePage />} />
      <Route path="/peer-tutor" element={<PeerTutor />} />
    </Routes>
    </div>
  );
};

export default App;
