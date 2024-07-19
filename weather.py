#Exercise 2: Exploring Python Libraries
#Use the requests library to fetch weather information from an online weather API (e.g., weatherapi.)
import requests
import json
# Replace with your OpenWeatherMap API key
api_key = "e2e37fed1027b0e000626306321cd29f" # Get your API key from https://openweathermap.org/

# City name to get weather for (replace with your desired city)
city = "Addis Ababa"

# Base URL for OpenWeatherMap API
base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Send GET request to fetch weather data
response = requests.get(base_url)

# Check for successful response
if response.status_code == 200:
  # Parse JSON response
  data = json.loads(response.text)
  
  # Extract relevant weather information
  weather_description = data["weather"][0]["description"]
  temperature = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius

  # Print weather information
  print(f"Weather in {city}: {weather_description}")
  print(f"Temperature: {temperature:.2f} °C")
else:
  # Handle unsuccessful request
  print(f"Error: Could not fetch weather data for {city}")
  print(f"Status code: {response.status_code}")