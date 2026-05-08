import React from 'react';
import ChosenRunHomeDisplay from './chosenRunHomeDisplay/chosenRunHomeDisplay';
import RunSummaryHomeDisplay from './runSummaryHomeDisplay/runSummaryHomeDisplay';

function HomeDisplay({ runID }) {
	if (runID === null) {
		return <RunSummaryHomeDisplay />;
	}

	return <ChosenRunHomeDisplay runID={runID} />;
}

export default HomeDisplay;