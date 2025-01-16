import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PeerTutor = () => {
    const [tutors, setTutors] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/peer_tutor/')
            .then((response) => {
                setTutors(response.data);
            })
            .catch((error) => {
                console.error('There was an error fetching the tutor data!', error);
            });
    }, []);

    return (
        <div style={{ padding: '20px' }}>
            <h1>Peer Tutors</h1>
            <ul>
                {tutors.map((tutor) => (
                    <li key={tutor.id}>
                        <h2>{tutor.tutor_name}</h2>
                        <p>Subject: {tutor.subject}</p>
                        <p>Description: {tutor.description}</p>
                        <p>Contact: {tutor.contact}</p>
                        <p>Availability: {new Date(tutor.availability).toLocaleString()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default PeerTutor;
