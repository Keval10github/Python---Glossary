const canvas = document.getElementById('doodleCanvas');
const ctx = canvas.getContext('2d');

// Python-themed doodle elements
function drawDoodle() {
    // Snake drawing
    ctx.beginPath();
    ctx.moveTo(50, 50);
    ctx.bezierCurveTo(100, 25, 150, 75, 200, 50);
    // Add more Python-related elements
}

// Search functionality
async function searchTerm() {
    const term = document.getElementById('searchInput').value;
    const response = await fetch(`/search?term=${term}`);
    displayResults(await response.json());
}

async function showAll() {
    const response = await fetch('/all');
    displayResults(await response.json());
}
