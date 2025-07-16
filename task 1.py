import requests
import matplotlib.pyplot as plt

# Fetch weather data
API_KEY = "your_openweathermap_api_key"
CITY = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Extract relevant data
labels = ['Temperature', 'Feels Like', 'Min Temp', 'Max Temp']
values = [
    data['main']['temp'],
    data['main']['feels_like'],
    data['main']['temp_min'],
    data['main']['temp_max']
]

# Plot data
plt.figure(figsize=(8, 5))
plt.bar(labels, values, color='skyblue')
plt.title(f"Weather Stats for {CITY}")
plt.ylabel("Temperature (°C)")
plt.show()
