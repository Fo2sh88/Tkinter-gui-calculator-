# create a wheather application that fetches and displays weather data for a given location
import requests
import json
from datetime import datetime


def get_coordinates(city_name):
    # This is a docstring that explains what the function does.
    """Fetch the latitude and longitude for a given location using OpenCage Geocoding API"""
    # Create a URL string using f-string that will send the city name to the Open-Meteo Geocoding API
    geocoding_url = f"https://api.opencagedata.com/geocode/v1/json?q={city_name}&count=1&language=en&format=json"
    
    try:
        response = requests.get(geocoding_url)
        data = response.json()
        
        if data['results']:
            latitude = data['results'][0]['geometry']['lat']
            longitude = data['results'][0]['geometry']['lng']
            return latitude, longitude
        else:
            print("No results found for the specified city.")
            return None, None
    