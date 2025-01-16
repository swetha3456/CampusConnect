import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Welcome to CampusConnect</h1>
      <div>
        <Link to="/issue-center">
          <button>Issue Center</button>
        </Link>
        <Link to="/project-collaboration">
          <button>Project Collaborations</button>
        </Link>
        <Link to="/lost-and-found">
          <button>Lost and Found Hub</button>
        </Link>
        <Link to="/peer-tutor"><button>PeerTutor</button></Link>
      </div>
    </div>
  );
};

export default HomePage;
