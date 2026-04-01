import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [message, setMessage] = useState('Checking connection...');

  useEffect(() => {
    // Attempt to fetch from the FastAPI backend at http://localhost:8000
    fetch('http://localhost:8000/')
      .then((res) => res.json())
      .then((data) => setMessage(data.message || 'Connected!'))
      .catch((err) => setMessage('Error: Could not connect to backend.'));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Backend Status: <strong>{message}</strong>
        </p>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      </header>
    </div>
  );
}

export default App;
