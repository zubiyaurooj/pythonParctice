
import requests
import json
from datetime import datetime
import os

# ---------------------------
# File to store search history
HISTORY_FILE = "weather_history.txt"

# ---------------------------
# You can get a free API key from https://openweathermap.org/api
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ---------------------------
def fetch_weather(city):
    """Fetch weather info for a city using OpenWeatherMap API."""
    if API_KEY == "YOUR_API_KEY_HERE":
        print("⚠ Please add your OpenWeatherMap API key before running the program.")
        return None

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"   # to get temperature in Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check for invalid city or bad response
        if response.status_code != 200:
            print("❌ City not found or invalid input!")
            return None

        # Extract important data
        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].title(),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather

    except requests.exceptions.RequestException:
        print("⚠ Network error! Please check your internet connection.")
        return None


# ---------------------------
def save_history(weather):
    """Save weather info to a local file."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(weather) + "\n")


def view_history():
    """Display search history."""
    print("\n--- Search History ---")
    if not os.path.exists(HISTORY_FILE):
        print("No history found yet.")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("No previous searches.")
        return

    for line in lines:
        record = json.loads(line.strip())
        print(f"{record['time']} | {record['city']}, {record['country']} | "
              f"{record['temperature']}°C | {record['description']}")


# ---------------------------
def main():
    while True:
        print("\n========== Weather Information Fetcher ==========")
        print("1. Get Weather Info")
        print("2. View Search History")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("\nEnter city name: ")
            weather = fetch_weather(city)
            if weather:
                print(f"\n✅ Weather in {weather['city']}, {weather['country']}")
                print(f"🌡 Temperature: {weather['temperature']}°C")
                print(f"🌥 Condition: {weather['description']}")
                print(f"⏰ Fetched at: {weather['time']}")
                save_history(weather)

        elif choice == "2":
            view_history()

        elif choice == "3":
            print("👋 Exiting... Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Try again!")


# ---------------------------
if __name__ == "__main__":
    main()
