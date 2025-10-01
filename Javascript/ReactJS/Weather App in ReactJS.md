# 🌤️ Weather App in ReactJS

Create a simple weather forecast app using React and a weather API like [OpenWeatherMap](https://openweathermap.org/api). This is a great project to practice working with APIs, handling async requests, and managing form input.

---

## 🎯 Objective

Build a ReactJS application where users can enter a city and get current weather details like temperature, condition, and humidity.

---

## 🔧 Features

* Input a city name to fetch weather info
* Display temperature, weather condition, humidity, and wind speed
* Error message for invalid city names
* Optional: background changes based on weather condition

---

## 🧱 Project Structure

```
react-weather-app/
│
├── src/
│   ├── components/
│   │   └── WeatherCard.js
│   ├── App.js
│   └── index.css
│
└── public/
```

---

## 🛠️ Steps to Build

### 1. Set Up React App

```bash
npx create-react-app react-weather-app
cd react-weather-app
npm start
```

### 2. Get API Key

Sign up at [OpenWeatherMap](https://openweathermap.org/) and get your API key.

---

### 3. Implement Core Logic

#### Basic `App.js` Sample

```jsx
import React, { useState } from 'react';

const App = () => {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);

  const fetchWeather = async () => {
    try {
      const res = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=YOUR_API_KEY&units=metric`
      );
      const data = await res.json();
      if (data.cod === 200) {
        setWeather(data);
      } else {
        setWeather(null);
        alert('City not found');
      }
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="app">
      <h1>Weather App</h1>
      <input
        type="text"
        placeholder="Enter city..."
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <button onClick={fetchWeather}>Get Weather</button>

      {weather && (
        <div className="weather-card">
          <h2>{weather.name}</h2>
          <p>{weather.main.temp} °C</p>
          <p>{weather.weather[0].description}</p>
          <p>Humidity: {weather.main.humidity}%</p>
        </div>
      )}
    </div>
  );
};

export default App;
```

---

## 🎨 Bonus Ideas

* Show weather icons using OpenWeatherMap's icon set
* Animate loading state
* Convert units (°C ⇄ °F)
* Save search history

---

## 📦 Useful Tools

* [OpenWeatherMap API Docs](https://openweathermap.org/current)
* Axios (alternative to `fetch`)
* Tailwind CSS for styling
