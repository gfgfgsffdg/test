import requests
import json
import tkinter
from geopy.geocoders import Nominatim
#variables
response_raw = None
response_raw1 = []
wetter = None
userinput = None
geolocator = Nominatim(user_agent="JaysTkinterproject5969")
parameter = {"lat": None,"lon":None}
header = {"Accept": "application/json"}
#vars for formating json
response_raw = None
response_raw1 = []
response_raw2 = []
proccesed_condition = None
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
#tkinter head
root = tkinter.Tk()
root.geometry("500x500")
root.title("Wetter app")

#functions
def get_lat_and_long():
    global parameter
    userinput = wo.get()
    location = geolocator.geocode(userinput)
    get_weather_ant_temp(str(location.latitude), str(location.longitude))
    Das_wetter.config(text="Das Wetter ist " + proccesed_condition_auf_deutsch[proccesed_condition])
    die_temperatur.config(text="Die Temperatur beträgt " + str(temperatur) + "°")
#main
def get_weather_ant_temp(lat, long):
    global proccesed_condition
    global temperatur
    parameter["lat"] = lat
    parameter["lon"] = long
    response_raw = requests.get("https://api.brightsky.dev/current_weather", headers=header, params=parameter)
    #format the json and print at the end
    response_raw1 = response_raw.json()
    response_raw2 = response_raw1['weather']
    proccesed_condition = response_raw2["condition"]
    temperatur = int(response_raw2["temperature"])
    print(proccesed_condition)
    print(temperatur)
    #gui_update()
def gui_update(): #tkinter 
    global wo, proccesed_condition, proccesed_condition_auf_deutsch, Das_wetter, die_temperatur
    Das_wetter = tkinter.Label(root, text="Das Wetter ist " + proccesed_condition_auf_deutsch[proccesed_condition])
    Das_wetter.pack()
    die_temperatur = tkinter.Label(root, text="Die Temperatur beträgt " + str(temperatur) + "°")
    die_temperatur.pack()
    welche_stadt_label = tkinter.Label(root, text="Welche stadt?")
    welche_stadt_label.place(x=10, y=50)
    wo = tkinter.Entry(root)
    wo.pack()
    neu_laden = tkinter.Button(root, text="Neu laden", command=get_lat_and_long)
    neu_laden.pack()
    root.mainloop()


get_weather_ant_temp("52.52", "13.4")
gui_update()