import tkinter as tk
import requests
import time 

def getweather(win):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=588f0268b643ce51d26fb987245fb1b2"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]['main']
    temp = int(json_data["main"]["temp"]-273.15)
    min_temp = int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data["sys"]["sunrise"]))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data["sys"]["sunset"]))
    final_info = condition + "\n" + str(temp) + "degree celsius"
    final_data = "\n" + "Max Temp :" + str(max_temp) + "\n" + "Min Temp : " + str(min_temp) + "\n" + "Pressure :" + str(pressure) + "\n" + "Humidity :" + str(humidity) + "\n" + "Wind Speed:" + str(wind)+ "\n"+ "Sunrise :" + str(sunrise) + "\n" + "sunset :"+ str(sunset)

    label1.config(text = final_info)
    label2.config(text = final_data)

win = tk.Tk()
#win.geometry("600*500")
win.title("Weather App")

#choosing fonts size
f = ("poppins",15,"bold")
t = ("poppins",35,"bold")
textfield = tk.Entry(win,font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind("<Return>",getweather)

label1 = tk.Label(win, font = t)
label1.pack()

label2 = tk.Label(win,font = f)
label2.pack()
win.mainloop()
