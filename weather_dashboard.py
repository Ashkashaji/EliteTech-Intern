import requests
import matplotlib.pyplot as plt

city = "Thrissur"
api_key = "9ded8f6776f00c5439394c814084fae8"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
else:
    print(f"Error fetching data: {data}")
    exit()  # stop execution because API call failed


labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
values = [temp, humidity, pressure]
plt.bar(labels, values, color=['orange', 'blue', 'green'])
plt.title(f'Weather Data for {city}')
plt.show()
