import requests

# Use API KEYS
WEATHER_API_KEY = '02e6af2ce21331756fa768b8153aa386'
NEWS_API_KEY = 'aa3040bce33a4fdca1a26bc0e7c9cdea'

def get_weather(city):
    # URL to get current weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    #  If city is not found
    if data.get("cod") != 200:
        return "City not found!"

    #  Format the weather details
    weather = {
        "City": data["name"],
        "Temperature": f"{data['main']['temp']}°C",
        "Weather": data["weather"][0]["description"].title(),
        "Humidity": f"{data['main']['humidity']}%",
        "Wind": f"{data['wind']['speed']} m/s"
    }
    return weather

def get_news():
    # URL to get top headlines from India
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Check for errors in the response
    if data.get("status") != "ok":
        return ["Failed to fetch news."]

    articles = data.get("articles", [])

    # If there are no articles
    if not articles:
        return ["No news articles found."]

    # Extract top 3 headlines
    headlines = [article['title'] for article in articles[:3]]
    return headlines

def main():
    print("📍 Weather & News Dashboard")
    city = input("Enter your city name: ")

    # Fetch weather
    print("\n🔎 Fetching weather...")
    weather = get_weather(city)
    if isinstance(weather, str):
        print(weather)
    else:
        for key, value in weather.items():
            print(f"{key}: {value}")
    
    # Fetch news
    print("\n📰 Top News Headlines:")
    headlines = get_news()
    for i, title in enumerate(headlines, 1):
        print(f"{i}. {title}")

# Main program starts here
if __name__ == "__main__":
    main()