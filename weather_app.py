import requests

# Replace with your own API key
API_KEY = "0ce71c2ed8445f996b5cc9d5efce08cc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Ask user for city name
city = input("Enter city name: ")

# Build request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]

    temperature = main['temp']
    humidity = main['humidity']
    description = weather['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
else:
    print("Error fetching data. Please check the city name or API key.")
