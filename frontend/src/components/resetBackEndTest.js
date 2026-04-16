import React from 'react';

function ResetBackEndTest() {
    const handleClick = async () => {
        await fetch('http://localhost:5000/api/reset', {
            method: 'POST',
        });
        alert('Back-end reset successfully!');
    }

    return (
        <button onClick={handleClick}>
            Reset Back-end
        </button>
    );
}