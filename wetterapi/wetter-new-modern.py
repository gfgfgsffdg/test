import requests
import json
import customtkinter
from geopy.geocoders import Nominatim
#variables
response_raw = None
response_raw1 = []
wetter = None
userinput = None
geolocator = Nominatim(user_agent="customtkinterpCTKroject5969")
parameter = {"lat": None,"lon":None}
header = {"Accept": "application/json"}
#vars for formating json
response_raw = None
response_raw1 = []
response_raw2 = []
proccesed_condition = None
icon_plaintext = None
weather_icons = {
    "clear-day": "☀️",  # Sun
    "clear-night": "🌙",  # Moon
    "partly-cloudy-day": "🌤️",  # Sun behind cloud
    "partly-cloudy-night": "🌥️",  # Moon behind cloud
    "cloudy": "☁️",  # Cloud
    "fog": "🌫️",  # Fog
    "wind": "🌬️",  # Wind face
    "rain": "🌧️",  # Cloud with rain
    "sleet": "🌨️",  # Cloud with snow and rain
    "snow": "❄️",  # Snowflake
    "hail": "🌩️",  # Cloud with hail
    "thunderstorm": "⛈️",  # Cloud with lightning and rain
    "null": "❓"  # Question mark
}
proccesed_condition_auf_deutsch = {
    "dry": "trocken",
    "fog": "Nebel",
    "rain": "Regen",
    "sleet": "Schneeregen",
    "snow": "Schnee",
    "hail": "Hagel",
    "thunderstorm": "Gewitter",
    "null": "null"
}
temperatur = None
#customtkinter CTKhead
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500")
root.title("Wetter app")

#functions
def get_lat_and_long():
    global parameter
    userinput = wo.get()
    location = geolocator.geocode(userinput)
    get_weather_ant_temp(str(location.latitude), str(location.longitude))
    Das_wetter.configure(text="Das Wetter ist " + proccesed_condition_auf_deutsch[proccesed_condition])
    die_temperatur.configure(text="Die Temperatur beträgt " + str(temperatur) + "°")
#main
def get_weather_ant_temp(lat, long):
    global proccesed_condition
    global temperatur
    global icon_plaintext
    parameter["lat"] = lat
    parameter["lon"] = long
    response_raw = requests.get("https://api.brightsky.dev/current_weather", headers=header, params=parameter)
    #format the json and print at the end
    response_raw1 = response_raw.json()
    response_raw2 = response_raw1['weather']
    proccesed_condition = response_raw2["condition"]
    temperatur = int(response_raw2["temperature"])
    icon_plaintext = response_raw2["icon"]

    #gui_update()
def gui_update(): #customtkinter CTK

    global wo, proccesed_condition, proccesed_condition_auf_deutsch, Das_wetter, die_temperatur, root, weather_icons, icon_plaintext, icon
    Das_wetter = customtkinter.CTkLabel(root, text="Das Wetter ist " + proccesed_condition_auf_deutsch[proccesed_condition], font=("arial", 20))
    Das_wetter.pack(pady=5)
    die_temperatur = customtkinter.CTkLabel(root, text="Die Temperatur beträgt " + str(temperatur) + "°", font=("arial", 20))
    die_temperatur.pack(pady=5)
    welche_stadt_label = customtkinter.CTkLabel(root, text="Welche tadt?", font=("arial", 20))
    welche_stadt_label.place(x=5, y=80)
    wo = customtkinter.CTkEntry(root)
    wo.pack(pady=5)
    neu_laden = customtkinter.CTkButton(root, text="Neu laden", command=get_lat_and_long)
    neu_laden.pack(pady=15)
    icon = customtkinter.CTkLabel(root, text=weather_icons[icon_plaintext], font=("arial", 50))
    icon.place(x=10, y=5)
    root.mainloop()


get_weather_ant_temp("52.52", "13.4")
gui_update()