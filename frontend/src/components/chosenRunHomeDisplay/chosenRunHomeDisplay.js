import React, { useEffect, useState } from 'react'
import { getBriefDataFromRunID, getRunDataPointsFromRunID } from '../../api/runsApi'
import { formatMiles, formatMph, formatFeet, formatDateMonthDay } from '../../utils/conversions'
import "./chosenRunHomeDisplay.css"
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import L from 'leaflet';

// Icons for the map markers
const startIcon = L.divIcon({
    className: '',
    html: `
        <div style="
            width: 16px;
            height: 16px;
            background: green;
            border: 3px solid white;
            border-radius: 50%;
        "></div>
    `,
    iconSize: [16, 16],
    iconAnchor: [8, 8]
});

const finishIcon = L.divIcon({
    className: '',
    html: `
        <div style="
            width: 18px;
            height: 18px;
            border-radius: 50%;
            border: 3px solid white;
            background:
                repeating-conic-gradient(
                    black 0% 25%,
                    white 25% 50%
                ) 50% / 8px 8px;
        "></div>
    `,
    iconSize: [18, 18],
    iconAnchor: [9, 9]
});


// component to display the chosen run's data on the home page, including a map with the run's path and summary statistics
function ChosenRunHomeDisplay({ runID }) {
	const [runData, setRunData] = useState(null);
	const [runDataPoints, setRunDataPoints] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	useEffect(() => {
		if (runID == null) {
			return;
		}

		setLoading(true);
		setError(null);

		async function load() {
			try {
				const briefData = await getBriefDataFromRunID(runID);
				setRunData(briefData);

				const points = await getRunDataPointsFromRunID(runID);

				if (!points || typeof points !== 'object') {
					throw new Error('Invalid points data structure');
				}

				const orderedPoints = Object.keys(points)
					.sort((a, b) => parseInt(a) - parseInt(b))
					.map(key => {
						const p = points[key];
						return {
							lat: parseFloat(p.lat),
							lon: parseFloat(p.lon),
							elevation: p.elevation,
							timestamp: p.timestamp
						};
					});

				setRunDataPoints(orderedPoints);
			} catch (err) {
				console.error('Error loading run data:', err);
				setError(err.message);
				setRunDataPoints([]);
			} finally {
				setLoading(false);
			}
		}

		load();
	}, [runID]);

	if (loading) return <div>Loading...</div>;

	if (error) return <div>Error loading run: {error}</div>;

	if (runData && Array.isArray(runDataPoints) && runDataPoints.length > 0) {
		const validPoints = runDataPoints.filter(point => point && point.lat != null && point.lon != null && !isNaN(point.lat) && !isNaN(point.lon));

		if (validPoints.length === 0) {
			return <div>No valid GPS data available for this run.</div>;
		}

		const startPoint = validPoints[0];
		const endPoint = validPoints[validPoints.length - 1];

		console.log('Start Point:', startPoint);
		console.log('End Point:', endPoint);

		if (!startPoint || isNaN(startPoint.lat) || isNaN(startPoint.lon) || !endPoint || isNaN(endPoint.lat) || isNaN(endPoint.lon)) {
			return <div>Invalid GPS coordinates for map display.</div>;
		}
		const formattedDate = formatDateMonthDay(runData.date);
		const distanceMiles = formatMiles(runData.total_distance);
		const averageSpeedMph = formatMph(runData.avg_pace);
		const ascentFeet = formatFeet(runData.ascent);

		return (
			<div>
				<div>
					<h2>Run ID: {runData.id}</h2>
					<div className='chosenRunHomeDisplayActivitySummaryBox'>
						<p className='chosenRunHomeDisplayActivitySummaryBoxElement'>Date: {formattedDate}</p>
						<p className='chosenRunHomeDisplayActivitySummaryBoxElement'>Distance: {distanceMiles} mi</p>
						<p className='chosenRunHomeDisplayActivitySummaryBoxElement'>Avg Speed: {averageSpeedMph} mph</p>
						<p className='chosenRunHomeDisplayActivitySummaryBoxElement'>Ascent: {ascentFeet} ft</p>
					</div>
				</div>

				<div>
					<MapContainer center={[startPoint.lat, startPoint.lon]} zoom={13} style={{ height: "400px", width: "100%" }}>
						<TileLayer
							url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
						/>
						<Polyline positions={validPoints.map(point => [point.lat, point.lon])} color="blue" />
						{/* Add start and end markers */}
						<Marker icon={startIcon} position={[startPoint.lat, startPoint.lon]}></Marker>
						<Marker icon={finishIcon} position={[endPoint.lat, endPoint.lon]}></Marker>

					</MapContainer>
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