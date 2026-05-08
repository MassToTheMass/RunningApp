import React, { useRef } from 'react';

import './homeSideBar.css';

function HomeSideBar({ runs, onSelectRun, fetchRuns }) {
    const fileInputRef = useRef(null);

    const handleClick = () => {
        fileInputRef.current.click();
    };

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        if (selectedFile) {
            uploadFile(selectedFile);
        }
    };

    const uploadFile = async (file) => {
        const formData = new FormData();
        formData.append('file', file);

        await fetch('http://localhost:5000/api/upload', {
            method: 'POST',
            body: formData,
        });

        fetchRuns();
        alert('File uploaded successfully!');
    };

    return (
        <div className="runsContainer">
            <h1>Upload A Run</h1>
            <input type="file" ref={fileInputRef} style={{ display: 'none' }} onChange={handleFileChange} />
            <button className="sidebarbutton" onClick={handleClick}>Upload</button>

            <h1>Recent Runs</h1>
            {runs.map(run => (
                <button className="sidebarbuttonrun" key={run.id} onClick={() => onSelectRun(run.id)}>{new Date(run.date).toLocaleDateString('en-US', {
                    month: 'short',
                    day: 'numeric'
                })} km</button>
            ))}
        </div>
    )
}

export default HomeSideBar;