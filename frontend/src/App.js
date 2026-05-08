import './App.css';

import HomeSideBar from './components/homeSideBar/homeSideBar';
import HomeDisplay from './components/homeDisplay';
import React, { useState } from 'react';

import { useRuns } from './hooks/useRuns';

function App() {
  const { runs, fetchRuns } = useRuns();
  const [selectedRunID, setSelectedRunID] = useState(null);

  return (
    <div className="App">
      <div className="container">
        <div className="sidebar">
          <HomeSideBar runs={runs} onSelectRun={setSelectedRunID} fetchRuns={fetchRuns} />
        </div>
        <div className="content">
          <h1>Running App</h1>
          <HomeDisplay runID={selectedRunID} />
        </div>
      </div>
    </div>
  );
}

export default App;
