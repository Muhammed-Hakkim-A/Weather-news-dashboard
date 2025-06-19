# Weather-news-dashboard
# 🌦 Weather & News Dashboard

A simple Python project that displays *current weather* and the *top 3 news headlines* for users in India.

---

## 🔧 Features

- 📍 Enter any city name to fetch weather info
- 🌡 Get temperature, humidity, and wind speed
- 📰 View top 3 latest news headlines from India
- 🚫 Handles errors like invalid city names or API issues

---

## 🚀 Technologies Used

- Python 3
- Requests library
- OpenWeatherMap API
- NewsAPI.org

---

## 📦 How to Run

1. Install required library:
   ```bash
   pip install requests
   
2. Add your API keys inside the script:

WEATHER_API_KEY = 'your_openweathermap_api_key'
NEWS_API_KEY = 'your_newsapi_key'


3. Run the Python script:

python weather_news_dashboard.py




---

🧪 Sample Output

📍 Weather & News Dashboard
Enter your city name: Kochi

🔎 Fetching weather...
City: Kochi
Temperature: 30°C
Weather: Clear Sky
Humidity: 60%
Wind: 3.6 m/s

📰 Top News Headlines:
1. India launches new space mission
2. Rainfall expected across Kerala
3. Tech industry sees major hiring boost


---

📁 File Structure

weather_news_dashboard/
├── weather_news_dashboard.py
├── README.md
└── .gitignore (optional)


---

👤 Author

Hakkim
BCA Student | Python Learner | Aspiring Full Stack Developer
GitHub | LinkedIn


---

💡 Future Improvements

Add a GUI using Tkinter or Flask

Auto-location detection using IP address

Option to toggle °C and °F

5-day weather forecast
