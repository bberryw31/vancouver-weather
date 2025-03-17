import requests

import json


url = "https://api.openweathermap.org/data/2.5/forecast?id=6173331&APPID=29c03c1ee13d8bb534a57f04fd9bc6d6"
response = requests.get(url)

vancouver_weather = json.loads(response.text)
print(vancouver_weather)

weather_details = vancouver_weather['list']
print('Current weather in Vancouver:')
print(weather_details[0]['weather'][0]['main'], '-', weather_details[0]['weather'][0]['description'])