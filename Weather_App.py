"""
Weather App - A Simple Weather Application
Fetches real-time weather data from Open-Meteo API
"""

import requests
from tkinter import Tk, Label, Entry, Button, messagebox, StringVar


# ==================== CONSTANTS ====================
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
BG_COLOR = "#2c3e50"
ACCENT_COLOR = "#3498db"
TEXT_COLOR = "white"

WEATHER_CONDITIONS = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Foggy",
    51: "Light drizzle",
    61: "Slight rain",
    80: "Slight rain showers",
    95: "Thunderstorm"
}


# ==================== API FUNCTIONS ====================
def get_weather(city):
    """
    Fetch weather data for a given city using Open-Meteo API.
    
    Args:
        city (str): City name to search for
        
    Returns:
        dict: Weather data or None if not found
    """
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    
    try:
        # Get city coordinates
        geo_response = requests.get(geocoding_url, timeout=5)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        
        if "results" not in geo_data or len(geo_data["results"]) == 0:
            return None
        
        # Extract location information
        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "Unknown")
        
        # Fetch weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
        
        weather_response = requests.get(weather_url, timeout=5)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        # Add location info to response
        weather_data["location_name"] = city_name
        weather_data["location_country"] = country
        
        return weather_data
        
    except requests.exceptions.RequestException as e:
        messagebox.showerror("API Error", f"Failed to fetch data: {str(e)}")
        return None


def format_weather_display(data):
    """
    Format weather data for display.
    
    Args:
        data (dict): Weather data from API
        
    Returns:
        str: Formatted weather information
    """
    if data is None:
        return None
    
    if "current" in data:
        city = data["location_name"]
        country = data["location_country"]
        temp_c = data["current"]["temperature_2m"]
        humidity = data["current"]["relative_humidity_2m"]
        wind_kph = data["current"]["wind_speed_10m"]
        weather_code = data["current"]["weather_code"]
        condition = WEATHER_CONDITIONS.get(weather_code, "Unknown")
        
        return f"""
╔════════════════════════════════════════╗
║  Weather in {city}, {country}
╠════════════════════════════════════════╣
║  🌡️  Temperature: {temp_c}°C
║  ☁️  Condition: {condition}
║  💧 Humidity: {humidity}%
║  💨 Wind Speed: {wind_kph} km/h
╚════════════════════════════════════════╝
        """
    return None


# ==================== GUI APPLICATION ====================
def create_gui():
    """Create and run the GUI application."""
    
    # Create main window
    root = Tk()
    root.title("Weather App")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.configure(bg=BG_COLOR)
    root.resizable(False, False)
    
    # Title Label
    title_label = Label(
        root,
        text="🌤️  Weather Application  🌤️",
        font=("Helvetica", 24, "bold"),
        bg=BG_COLOR,
        fg=ACCENT_COLOR
    )
    title_label.pack(pady=20)
    
    # Description Label
    desc_label = Label(
        root,
        text="Get real-time weather information for any city",
        font=("Helvetica", 10),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    )
    desc_label.pack(pady=5)
    
    # City Input Label
    city_label = Label(
        root,
        text="Enter City Name:",
        font=("Helvetica", 12, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    )
    city_label.pack(pady=(20, 5))
    
    # City Input Entry Field
    city_entry = Entry(
        root,
        font=("Helvetica", 14),
        width=30,
        bg=ACCENT_COLOR,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR
    )
    city_entry.pack(pady=10)
    
    # Result Display Label
    result_label = Label(
        root,
        text="",
        font=("Courier", 11),
        bg=BG_COLOR,
        fg=ACCENT_COLOR,
        justify="left"
    )
    result_label.pack(pady=20)
    
    def search_weather():
        """Search for weather when button is clicked."""
        city = city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name!")
            return
        
        data = get_weather(city)
        
        if data is None:
            messagebox.showerror("Error", f"City '{city}' not found. Please try another city.")
            result_label.config(text="")
            return
        
        weather_text = format_weather_display(data)
        if weather_text:
            result_label.config(text=weather_text)
        else:
            messagebox.showerror("Error", "Could not fetch weather data.")
    
    # Search Button
    search_button = Button(
        root,
        text="🔍 Search Weather",
        font=("Helvetica", 12, "bold"),
        command=search_weather,
        bg=ACCENT_COLOR,
        fg=TEXT_COLOR,
        activebackground="#2980b9",
        width=20
    )
    search_button.pack(pady=10)
    
    # Exit Button
    exit_button = Button(
        root,
        text="Exit",
        font=("Helvetica", 10),
        command=root.quit,
        bg="#e74c3c",
        fg=TEXT_COLOR,
        activebackground="#c0392b",
        width=20
    )
    exit_button.pack(pady=5)
    
    # Allow Enter key to search
    city_entry.bind('<Return>', lambda event: search_weather())
    
    root.mainloop()


# ==================== MAIN ====================
if __name__ == "__main__":
    create_gui()