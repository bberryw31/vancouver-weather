import requests

import json


url = "https://api.openweathermap.org/data/2.5/forecast?id=6173331&APPID=29c03c1ee13d8bb534a57f04fd9bc6d6"
response = requests.get(url)

vancouver_weather = json.loads(response.text)

weather_details = vancouver_weather['list']
print('Weather in Vancouver:')
for date in range(32, 40):
    print(weather_details[date]['dt_txt'], '-', weather_details[date]['weather'][0]['description'])