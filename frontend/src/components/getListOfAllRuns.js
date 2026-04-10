import React from 'react';

function GetListOfAllRuns({ runs }) {
    return (
        <div class="runsContainer">
            <h1>List of All Runs</h1>
            {runs.map(run => (
                <button class="sidebarbuttonrun" key={run.id}>{run.date} km</button>
            ))}
        </div>
    )
}

export default GetListOfAllRuns;