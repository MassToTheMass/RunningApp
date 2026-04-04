import React, { useEffect } from 'react';

function GetListOfAllRuns({ runs }) {
    return (
        <div>
            <h1>List of All Runs</h1>
            <ul>
                {runs.map(run => (
                    <li key={run.id}>{run.date} - {run.distance} km</li>
                ))}
            </ul>
        </div>
    )
}

export default GetListOfAllRuns;