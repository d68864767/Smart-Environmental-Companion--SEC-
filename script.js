```javascript
// Fetching data from the server and updating the UI
function updateUI() {
    fetch('/status')
        .then(response => response.json())
        .then(data => {
            // Update the UI with the data
            document.getElementById('temperature').innerText = data.environment.temperature;
            document.getElementById('humidity').innerText = data.environment.humidity;
            document.getElementById('airQuality').innerText = data.environment.air_quality;
            document.getElementById('lighting').innerText = data.environment.lighting;
            document.getElementById('energyUsage').innerText = data.energy.usage;
            document.getElementById('healthStatus').innerText = data.health.status;
        });
}

// Sending user inputs to the server
function sendUserInput(input) {
    fetch('/input', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(input),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response
        console.log(data);
    });
}

// Updating the UI every second
setInterval(updateUI, 1000);
```
