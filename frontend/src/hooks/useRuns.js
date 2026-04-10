import { useState, useEffect } from 'react';
import { getRunsForSideBar } from '../api/runsApi';

export function useRuns() {
    const [runs, setRuns] = useState([]);

    const fetchRuns = async () => {
        getRunsForSideBar().then(data => setRuns(data));
    };

    useEffect(() => {
        fetchRuns();
    }, []);

    return { runs, fetchRuns };
}