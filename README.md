# Weather App 🌤️

A simple and elegant weather application built with Python that fetches real-time weather data from the Open-Meteo API and displays it in a modern GUI.

## Features ✨

- 🌍 Search weather for any city in the world
- 🌡️ Display temperature in Celsius
- 💧 Show humidity percentage
- 💨 Display wind speed
- ☁️ Show weather condition
- 🎨 Modern, professional GUI interface
- ⚡ Fast and responsive

## Requirements 📋

- Python 3.7+
- requests library
- tkinter (usually comes with Python)

## Installation 🚀

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Python-projects
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   - **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:
```bash
pip install requests
```

## Usage 🎯

Run the application:
```bash
python Weather_App.py
```

1. Enter a city name in the input field
2. Click "🔍 Search Weather" or press Enter
3. View the weather information for that city

## API Used 🔌

This project uses the **Open-Meteo API** which is:
- Free (no API key required)
- Open source
- Reliable and fast

Visit: https://open-meteo.com

## Project Structure 📁

```
Weather_App.py          # Main application file
.gitignore              # Git ignore file
README.md              # Project documentation
```

## Code Features 💻

- **Modular Design:** Separated functions for API calls and UI
- **Error Handling:** Proper exception handling and user feedback
- **Constants:** All configuration values at the top
- **Documentation:** Docstrings for all functions
- **User-Friendly:** Enter key support and clear error messages

## Author 👨‍💻

Created by You

## License 📄

This project is open source and available under the MIT License.

## Future Enhancements 🚀

- [ ] Add temperature unit toggle (°C / °F)
- [ ] Add weather forecast for next days
- [ ] Add saved favorite cities
- [ ] Add weather alerts
- [ ] Dark/Light theme toggle
