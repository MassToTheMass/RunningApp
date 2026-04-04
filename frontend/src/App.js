import './App.css';

import getListOfAllRuns from './components/getListOfAllRuns';
import FileUpload from './components/fileUpload';
import React, { useEffect, useState} from 'react';


function App() {
  return (
    <div className="App">
		<h1>Running App</h1>
		<FileUpload />
		<getListOfAllRuns />
    </div>
  );
}

export default App;
