document.addEventListener('DOMContentLoaded', function () {
    // Create a map centered at latitude 0, longitude 0 with zoom level 2
    var map = L.map("map").setView([10.241, -67.957], 10);

// Add a tile layer (you can choose different tile layers, e.g., OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Add a marker at latitude 0, longitude 0
L.marker([0, 0]).addTo(map)
    .bindPopup('Hello, Leaflet!');

});