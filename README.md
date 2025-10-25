This is a Python-based weather dashboard that fetches and visualizes current weather data (temperature, humidity, and pressure) for a given city using the OpenWeatherMap API and matplotlib.
Here’s a simple README.md you can use for your weather_dashboard.py project.

Features

- Fetches real-time weather data using OpenWeatherMap API
- Displays temperature (°C), humidity (%), and pressure (hPa)
- Visualizes data using a bar chart (matplotlib)

Requirements

- Python 3.x
- requests
- matplotlib

Setup

1. Clone this repository:
   
   git clone https://github.com/Ashkashaji/EliteTech-Intern.git
   

2. Navigate to the project directory:
   
   cd EliteTech-Intern
   

3. Install dependencies:
   
   pip install -r requirements.txt
   

4. Add your OpenWeatherMap API key in `weather_dashboard.py`:
   python
   api_key = "YOUR_API_KEY"
   

Usage

Run the script:


python weather_dashboard.py


The script will:
- Request weather data for the specified city
- Display a bar chart with temperature, humidity, and pressure

Output

A simple bar chart representing the weather conditions of the entered city.

License

This project is for educational purposes under the Elite Tech Intern program.
