

export const getRunsForSideBar = async () => {
    const response = await fetch('http://localhost:5000/api/runsRecentTen');
    const data = await response.json();
    return data;
};

export const uploadGPXFile = async (formData) => {
    await fetch('http://localhost:5000/api/upload', {
        method: 'POST',
        body: formData,
    });
}