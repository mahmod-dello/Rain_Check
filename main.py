import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("path/to/.env")  # loading the environment variables file

# -------------------------------- Constants -------------------------------- #

LAT = 32.060253  # latitude
LONG = 118.796875  # longitude
OMW_API = "https://api.openweathermap.org/data/2.8/onecall"  # openweathermap API endpoint.
OMW_API_KEY = os.getenv("OMW_API_KEY")  # your openweathermap API key
ACC_SID = os.getenv("ACC_SID")  # your twilio Account SID
AUTH_TOKEN = os.getenv("AUTH_TOKEN")  # your twilio Account Authentication Token.

# os.getenv returns 'None' if the variable not set in your .env file

# -------------------------------- Script -------------------------------- #

# Openweathermap API parameters
weather_parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily",
    "appid": OMW_API_KEY
}

response = requests.get(url=OMW_API, params=weather_parameters)
response.raise_for_status()

weather_data = response.json()
print(weather_data)
weather_sliced = weather_data["hourly"][:12]  # holding the weather data of the next 12 hours

will_rain = False  # weather boolean flag
for hour_data in weather_sliced:
    condition_code = hour_data["weather"][0]["id"]  # access each hour's condition id (Read API Documentation)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(username=ACC_SID, password=AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella with you ☔.",
        from_="",
        to=""
    )
    # from_= your twilio phone number.
    # to= your actual phone number.
    print(message.status)  # queued mean sent successfully
