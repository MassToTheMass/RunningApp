import './App.css';

import FileUpload from './components/fileUpload';
import GetListOfTenRecentRuns from './components/homeSideBar/getListOfTenRecentRuns';
import HomeDisplay from './components/homeDisplay';
import React, { useEffect, useState } from 'react';

import { useRuns } from './hooks/useRuns';

function App() {
  const { runs, fetchRuns } = useRuns();
  const [selectedRunID, setSelectedRunID] = useState(null);

  return (
    <div className="App">
      <div className="container">
        <div className="sidebar">
          <h2>Running App</h2>
          <FileUpload fetchRuns={fetchRuns} />
          <GetListOfTenRecentRuns runs={runs} onSelectRun={setSelectedRunID} />
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
