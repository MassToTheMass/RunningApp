import React from 'react';

function GetListOfTenRecentRuns({ runs, onSelectRun }) {
    return (
        <div className="runsContainer">
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

export default GetListOfTenRecentRuns;