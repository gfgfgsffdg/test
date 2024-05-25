import requests
# import json
import customtkinter
from geopy.geocoders import Nominatim
from PIL import Image
# variables
response_raw = None
response_raw1 = []
wetter = None
userinput = None
geolocator = Nominatim(user_agent="customtkinterpCTKroject5969")
parameter = {"lat": None, "lon": None}
header = {"Accept": "application/json"}
# vars for formating json
response_raw = None
response_raw1 = []
response_raw2 = []
proccesed_condition = None
icon_plaintext = None
weather_icons = {
    # Sun
    "clear-day": customtkinter.CTkImage(dark_image=Image.open("clear-day.png"), size=(50, 50)),
    # Moon
    "clear-night": customtkinter.CTkImage(dark_image=Image.open("clearnight.png"), size=(50, 50)),
    # Sun behind cloud
    "partly-cloudy-day": customtkinter.CTkImage(dark_image=Image.open("partly_cloudy_day.png"), size=(50, 50)),
    # Moon behind cloud
    "partly-cloudy-night": customtkinter.CTkImage(dark_image=Image.open("barely_cloudy_night.png"), size=(50, 50)),
    # Cloud
    "cloudy": customtkinter.CTkImage(dark_image=Image.open("cloudy.png"), size=(50, 50)),
    # Fog
    "fog": customtkinter.CTkImage(dark_image=Image.open("fog.png"), size=(50, 50)),
    # Wind face
    "wind": customtkinter.CTkImage(dark_image=Image.open("wind.png"), size=(50, 50)),
    # Cloud with rain
    "rain": customtkinter.CTkImage(dark_image=Image.open("rain.png"), size=(50, 50)),
    # Cloud with snow and rain
    "sleet": customtkinter.CTkImage(dark_image=Image.open("sleet.png"), size=(50, 50)),
    # Snowflake
    "snow": customtkinter.CTkImage(dark_image=Image.open("rain.png"), size=(50, 50)),
    # Cloud with hail
    "hail": customtkinter.CTkImage(dark_image=Image.open("hail.png"), size=(50, 50)),
    # Cloud with lightning and rain
    "thunderstorm": customtkinter.CTkImage(dark_image=Image.open("thunderstorm.png"), size=(50, 50)),
    # Question mark
    "null": customtkinter.CTkImage(dark_image=Image.open("null.png"), size=(50, 50))
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
# customtkinter CTKhead
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500")
root.title("Wetter app")

# functions
def get_lat_and_long():
    global parameter
    global error, icon_plaintext, weather_icons, icon
    userinput = wo.get()
    location = geolocator.geocode(userinput)
    if location == None:
        error.configure(text="Error der Ort " + userinput + " wurde nicht gefunden")
    else:
        error.configure(text="")
        get_weather_ant_temp(str(location.latitude), str(location.longitude))
        Das_wetter.configure(text="Das Wetter ist " + proccesed_condition_auf_deutsch[proccesed_condition])
        die_temperatur.configure(text="Die Temperatur beträgt " + str(temperatur) + "°")
        icon.configure(image=weather_icons[icon_plaintext])
        wo_wir_sind.configure(text=userinput)
# main

def get_weather_ant_temp(lat, long):
    global proccesed_condition
    global temperatur
    global icon_plaintext
    parameter["lat"] = lat
    parameter["lon"] = long
    response_raw = requests.get("https://api.brightsky.dev/current_weather", headers=header, params=parameter)
    # format the json
    response_raw1 = response_raw.json()
    response_raw2 = response_raw1['weather']
    proccesed_condition = response_raw2["condition"]
    temperatur = int(response_raw2["temperature"])
    icon_plaintext = response_raw2["icon"]
get_weather_ant_temp("52.52", "13.4")
# gui
wo_wir_sind = customtkinter.CTkLabel(root, text="berlin", font=("arial", 20))
wo_wir_sind.pack()
Das_wetter = customtkinter.CTkLabel(
root, text="Das Wetter ist " + proccesed_condition_auf_deutsch[proccesed_condition])
Das_wetter.pack(pady=5)
die_temperatur = customtkinter.CTkLabel(
root, text="Die Temperatur beträgt " + str(temperatur) + "°", font=("arial", 20))
die_temperatur.pack(pady=5)
welche_stadt_label = customtkinter.CTkLabel(
root, text="Welche Stadt?", font=("arial", 20))
welche_stadt_label.place(x=10, y=110)
wo = customtkinter.CTkEntry(root)
wo.pack(pady=5)
neu_laden = customtkinter.CTkButton(
root, text="Neu laden", command=get_lat_and_long)
neu_laden.pack(pady=15)
icon = customtkinter.CTkLabel(
root, image=weather_icons[icon_plaintext], text="")
icon.place(x=10, y=5)
error = customtkinter.CTkLabel(root, text="", text_color="red")
error.pack()
root.mainloop()
