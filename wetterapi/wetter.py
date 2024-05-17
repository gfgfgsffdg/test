import requests
import json
import tkinter
from geopy.geocoders import Nominatim
#import geopy
#variables

response_raw = None
response_raw1 = []
wetter = None
userinput = None
geolocator = Nominatim(user_agent="JaysTkinterproject5969")
parameter = {"lat":"52.52","lon":"13.4"}
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
#functions
def get_lat_and_long():
    global parameter
    userinput = wo.get()
    location = geolocator.geocode(userinput)
    parameter = {"lat": str(location.latitude), "lon": str(location.longitude)}
    get_weather_ant_temp()
    root.mainloop()
#main
def get_weather_ant_temp():
    global proccesed_condition
    global temperatur
    response_raw = requests.get("https://api.brightsky.dev/current_weather", headers=header, params=parameter)
    #format the json and print at the end
    response_raw1 = response_raw.json()
    response_raw2 = response_raw1['weather']
    proccesed_condition = response_raw2["condition"]
    temperatur = int(response_raw2["temperature"])
#tkinter
get_weather_ant_temp()
root = tkinter.Tk()
root.geometry("500x500")
root.title("Wetter app")


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