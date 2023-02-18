import requests 
import matplotlib.pyplot as plt

# Below is odenses latitude and longitude
lat = '55.403756'
long = '10.402370'
url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m'

response = requests.get(url)

temp = response.json()['hourly']['temperature_2m']
temp_24h = temp[:24]

plt.plot(temp_24h)
date = response.json()['hourly']['time'][0][:10] # This is todays date
plt.title(date)
plt.show()