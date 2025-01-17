// import React from 'react';
// import { Link } from 'react-router-dom';

// const LandingPage = () => {
//   return (
//     <div style={{ textAlign: 'center', marginTop: '50px' }}>
//       <h1>Welcome to CampusConnect</h1>
//       <p>Connect, Collaborate, and Solve Campus Issues.</p>
//       <Link to="/login">
//         <button>Login / Register</button>
//       </Link>
//     </div>
//   );
// };

// export default LandingPage;
import React from "react";
import { useNavigate } from "react-router-dom";
import "./LandingPage.css";

const LandingPage = () => {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate("/login");
  };

  return (
    <div className="landing-container">
      <div className="welcome-section">
        <div className="container2">
          <h2>Welcome To</h2>
          <h1 contentEditable>Campus &emsp; Central</h1>
        </div>
        <div id="building"></div>
      </div>

      <div className="cta-section">
        <div id="computer"></div>
        <p>College can be difficult. Let us help.</p>
        <button className="get-started-btn" onClick={handleGetStarted}>
          Get Started
        </button>
      </div>
    </div>
  );
};

export default LandingPage;
