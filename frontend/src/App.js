import './App.css';

import FileUpload from './components/fileUpload';
import GetListOfAllRuns from './components/getListOfTenRecentRuns';
import React, { useEffect, useState} from 'react';

import { useRuns } from './hooks/useRuns';

function App() {
  const { runs, fetchRuns } = useRuns();

  return (
    <div className="App">
      <div class="container">
        <div class="sidebar">
          <h2>Running App</h2>
            <FileUpload fetchRuns={fetchRuns} />
            <GetListOfAllRuns runs={runs} />
        </div>
        <div class="content">
          <h1>Running App</h1>
        </div>
      </div>
    </div>
  );
}

export default App;
