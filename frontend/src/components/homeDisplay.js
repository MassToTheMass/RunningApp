import React, { useEffect } from 'react';
import { getBriefDataFromRunID } from '../api/runsApi'
import './chosenRunHomeDisplay/chosenRunHomeDisplay';
import ChosenRunHomeDisplay from './chosenRunHomeDisplay/chosenRunHomeDisplay';
import RunSummaryHomeDisplay from './runSummaryHomeDisplay/runSummaryHomeDisplay';

function HomeDisplay(runID) {

	console.log(`value: ${runID}`);
	console.log(runID.runID)

	if (runID.runID === null) {
		console.log("returning summary home display")
		return (
			<RunSummaryHomeDisplay />
		);
	} else {
		console.log("Returning the chosen run home display with Id of:")
		console.log(runID)
		return (
			<ChosenRunHomeDisplay runID={runID} />
		)
	}
}

export default HomeDisplay;