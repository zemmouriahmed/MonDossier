document.addEventListener('DOMContentLoaded', () => {
    const searchBox = document.querySelector('.search-box');
    searchBox.addEventListener('keypress', setQuery);

    const apiKey = 'VOTRE_CLE_API';
    const baseUrl = 'https://api.openweathermap.org/data/2.5/weather?';

    function setQuery(evt) {
        if (evt.keyCode === 13) { // keyCode 13 est la touche Entrée
            getWeather(searchBox.value);
            searchBox.value = ''; // Efface la barre de recherche après la requête
        }
    }

    function getWeather(query) {
        fetch(`${baseUrl}q=${query}&units=metric&APPID=${apiKey}`)
            .then(weather => {
                return weather.json();
            }).then(displayResults);
    }

    function displayResults(weather) {
        let city = document.querySelector('.city-name');
        city.innerText = `${weather.name}, ${weather.sys.country}`;

        let temp = document.querySelector('.temperature');
        temp.innerHTML = `${Math.round(weather.main.temp)}<span>°C</span>`;

        let weatherDesc = document.querySelector('.weather-description');
        weatherDesc.innerText = weather.weather[0].main;

        let details = document.querySelector('.weather-details');
        details.innerHTML = `
            Vent: ${weather.wind.speed} km/h<br>
            Humidité: ${weather.main.humidity}%
        `;

        // Ajoutez ici plus de détails si vous le souhaitez
    }
});
