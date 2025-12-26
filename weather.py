import requests

def get_weather(city):
    api_key = "2be58664b7ff4638847175149252612"  
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        print(f"\nWeather in {location}:")
        print(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
