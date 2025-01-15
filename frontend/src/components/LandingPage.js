import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Welcome to CampusConnect</h1>
      <p>Connect, Collaborate, and Solve Campus Issues.</p>
      <Link to="/login">
        <button>Login / Register</button>
      </Link>
    </div>
  );
};

export default LandingPage;
