import requests
from django.conf import settings

def get_temperature(city_name):
        api_key = settings.OPENWEATHERMAP_API_KEY 

        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
        response = requests.get(weather_url)
        response.raise_for_status()
        data = response.json()
        
        if response.status_code != 200:
            return 'City not found'
        
        temperature = data['main']['temp']
        
        return temperature