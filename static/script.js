function getWeather() {
    var city = document.getElementById('cityInput').value;
    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('weatherInfo').innerHTML = `
                <h2>${data.place}</h2>
                <p>Temperature: ${data.temperature} K</p>
                <p>Sunrise: ${new Date(data.sunrise * 1000).toLocaleTimeString()}</p>
                <p>Sunset: ${new Date(data.sunset * 1000).toLocaleTimeString()}</p>
            `;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
