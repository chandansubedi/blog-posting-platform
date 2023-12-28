import requests
def get_weather_data(city_name):
    api_key = '8e9f2c1f4bd1916f31aceea38384cb28'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        # Handle the exception as needed
        print(f"Error fetching weather data: {e}")
        return None

def print_weather_data(city_name):
    weather_data = get_weather_data(city_name)

    if weather_data:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']} °F")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Icon: {weather_data['weather'][0]['icon']}")
    else:
        print("Unable to fetch weather data. Please try again later.")

# Print weather data for Pokhara
print_weather_data('Pokhara, NP')