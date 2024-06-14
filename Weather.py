import requests 
from plyer import notification

api = "https://api.openweathermap.org/data/2.5/weather?q=Balaju,Nepal&APPID=d6b75fa1f9aa999d313e52a7eb48918c"

response = requests.get(api)

data = response.json()
temp = round(data["main"]["temp"] - 272.15, 2)
feel_like = round(data["main"]["feels_like"] - 272.15, 2)
description = data["weather"][0]["description"] 
total = "Temperature: {}°C, Feel like: {}°C, Description: {}".format(temp, feel_like, description)
notification.notify(
    title= "Today's Weather",
    message= total,
    app_name= "Weather",
    app_icon= r"C:\Users\Deepam Sah\Desktop\Temp\favicon.ico"
)
