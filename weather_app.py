import requests

API_KEY = "0ce71c2ed8445f996b5cc9d5efce08cc"
# personal key from OpenWeatherMap (needed for authentication).
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# the endpoint for current weather data.

# Ask user for city name
city = input("Enter city name: ")

# Build request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
# & is just a separator between multiple parameters in the URL.
# Every API defines its own parameters in its documentation.
# For OpenWeatherMap, q, appid, and units are part of its specification.

# Send request
response = requests.get(url)
# Stores the server’s response in response.

if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]
    #[0] means “take the first item in the list.”
    #Every HTTP response has a status code:

#200 → OK (success)

#404 → Not found

#401 → Unauthorized (bad API key)

#500 → Server error

    temperature = main['temp']
    humidity = main['humidity']
    description = weather['description']
    # data['main'] pulls out the "main" section, which contains temperature and humidity.

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
else:
    print("Error fetching data. Please check the city name or API key.")


# JSON is a data format that is built on two basic structures:
# a) Objects (key–value pairs)

# Written as { "key": "value" }

# b) Arrays (ordered lists)

# Written as [ item1, item2, item3 ]

# JSON (JavaScript Object Notation) is a lightweight, text-based format used to store and 
# exchange semi-structured or unstructured data, especially in web APIs, configuration files, and 
# NoSQL databases. It’s human-readable, language-independent, and widely adopted across modern applications.
