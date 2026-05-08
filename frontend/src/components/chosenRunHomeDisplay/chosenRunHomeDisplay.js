import React, { useEffect, useState } from 'react'
import { getBriefDataFromRunID } from '../../api/runsApi'
import "./chosenRunHomeDisplay.css"

function ChosenRunHomeDisplay({ runID }) {
	const [runData, setRunData] = useState(null);
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		if (runID == null) {
			return;
		}

		setLoading(true);

		async function load() {
			try {
				setRunData(await getBriefDataFromRunID(runID));
			} catch (error) {
				console.log(error);
			} finally {
				setLoading(false);
			}
		}

		load();
	}, [runID]);

	console.log(runData);

	if (loading) return (<div>Loading...</div>);

	if (runData != null) {
		return (
			<div>
				<h2>Run ID: {runData.id}</h2>
				<div className='chosenRunHomeDisplayActivitySummaryBox'>
					<p className='chosenRunHomeDisplayActivitySummaryBoxElement'>Date: {runData.date}</p>
					<p className='chosenRunHomeDisplayActivitySummaryBoxElement'>Distance: {runData.total_distance}</p>
					<p className='chosenRunHomeDisplayActivitySummaryBoxElement'>Average Pace: {runData.avg_pace}</p>
					<p className='chosenRunHomeDisplayActivitySummaryBoxElement'>Ascent: {runData.ascent}</p>
				</div>
			</div>
		)
	}
	return (
		<div>
			<h2>This shouldn't appear.</h2>
		</div>
	)
}

export default ChosenRunHomeDisplay;