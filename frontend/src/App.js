import './App.css';
import React, { useEffect, useState} from 'react';


function App() {
  const [runs, setRuns] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/runs')
      .then(response => response.json())
      .then(data => setRuns(data));
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          {runs.length > 0 ? runs.map((run, index) => (
            <div key={index}>
              <p>Date: {run.date}</p>
              <p>Distance: {run.distance}</p>
              <p>Duration: {run.duration}</p>
              <p>Average Pace: {run.avg_pace}</p>
            </div>
          )) : <p>No runs available.</p>}
        </a>
      </header>
    </div>
  );
}

export default App;
