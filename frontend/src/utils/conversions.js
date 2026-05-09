export const metersToMiles = (meters) => {
  const value = Number(meters);
  return Number.isFinite(value) ? value / 1609.344 : 0;
};

export const metersPerSecondToMph = (mps) => {
  const value = Number(mps);
  return Number.isFinite(value) ? value * 2.2369362920544 : 0;
};

export const formatMiles = (meters, digits = 2) => {
  return metersToMiles(meters).toFixed(digits);
};

export const metersToFeet = (meters) => {
  const value = Number(meters);
  return Number.isFinite(value) ? value * 3.2808398950131 : 0;
};

export const formatFeet = (meters, digits = 0) => {
  return metersToFeet(meters).toFixed(digits);
};

export const formatDateMonthDay = (dateValue) => {
  const value = new Date(dateValue);
  if (Number.isNaN(value.getTime())) {
    return String(dateValue);
  }
  return value.toLocaleDateString('en-US', {
    month: 'short',
    day: '2-digit',
  });
};

export const formatMph = (mps, digits = 2) => {
  return metersPerSecondToMph(mps).toFixed(digits);
};
