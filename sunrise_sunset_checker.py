import requests
from datetime import datetime
 
def convert24(time):
    # Parse the time string into a datetime object
    t = datetime.strptime(time, '%I:%M:%S %p')
    # Format the datetime object into a 24-hour time string
    return t.strftime('%H:%M:%S')

#Api zdobywajace lokacje
location = input("Submit location:")
getLocation = 'https://nominatim.openstreetmap.org/?addressdetails=1&q={}&format=json&limit=1'

response = requests.get(getLocation.format(location)).json()

lat = response[0]['lat']
lon = response[0]['lon']
#Api uzyskujace dane o sloncu na podstawie lokacji
getSun = 'https://api.sunrise-sunset.org/json?lat={}&lng={}'

result = requests.get(getSun.format(lat, lon)).json()

#Api do pogody
getWet = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true'
info = requests.get(getWet.format(lat, lon)).json()
temp = info['current_weather']['temperature']
wind = info['current_weather']['windspeed']
#Konwersja na czas 24h
srise = convert24(result['results']['sunrise'])
sset = convert24(result['results']['sunset'])
#Wynik
print("The sunrise in %s is at %s and sunset at %s.\nThe temperature is %d degrees Celsus and wind speed is %d km/h."%(location, srise, sset, temp, wind))
