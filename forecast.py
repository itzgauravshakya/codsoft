from tkinter import*
import requests
import json
from datetime import datetime

root =Tk()
root.title("Weather Forecast")
root.geometry("600x600") #size of the window by default
root.config(bg="skyblue")
root.resizable(0,0)

def time_format_for_location(utc):
    local_time = datetime.utcfromtimestamp(utc)
    return local_time.time()

city_value = StringVar()

def showWeather():
    api_key = "ce26548e8d53c3f3f3195f7ac65f99af"
    city_name=city_value.get()
    weather_url = (f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
    response = requests.get(weather_url) 
    weather_info = response.json() # changing response from json to python readable
    tfield.delete('1.0', 'end')   #to clear the text field for every new output

#as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
        temp = int(weather_info['main']['temp'] - kelvin)                                     #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nWindspeed: {wind_speed}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output


city_head= Label(root, text = 'Enter City Name', font = 'Arial 26 bold',bg='grey').pack(pady=10)
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold',bg='pink').pack()
Button(root, command = showWeather, text = "Check Weather", font="Arial 10 bold", bg='green', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
tfield = Text(root, width=46, height=10,bg='pink')
tfield.pack()

root.mainloop()