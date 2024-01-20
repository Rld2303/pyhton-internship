import requests
import datetime as dt

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric', 
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
            }
            return weather_info
        else:
            return {'error': f"Error: {data['message']}"}
    except Exception as e:
        return {'error': f"An error occurred: {e}"}

def main():
    api_key = '868c865f6a2cfda972a5e116ee6d0044'
    city = input("Enter the city name: ")

    weather_info = get_weather(api_key, city)

    if 'error' in weather_info:
        print(weather_info['error'])
    else:
        print(f"Weather in {weather_info['city']}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Description: {weather_info['description']}")

if __name__ == "__main__":
    main()


