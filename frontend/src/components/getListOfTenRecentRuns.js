import React from 'react';

function GetListOfTenRecentRuns({ runs }) {
    return (
        <div class="runsContainer">
            <h1>Recent Runs</h1>
            {runs.map(run => (
                <button class="sidebarbuttonrun" key={run.id}>{run.date} km</button>
            ))}
        </div>
    )
}

export default GetListOfTenRecentRuns;