import tkinter as tk
from tkinter import messagebox
import requests
# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        # Extract the data
        main_data = data["main"]
        weather_data = data["weather"][0]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        description = weather_data["description"]
        # Update the output labels
        temp_label.config(text=f"Temperature: {temperature}°C")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        humidity_label.config(text=f"Humidity: {humidity}%")
        description_label.config(text=f"Description: {description.capitalize()}")
    else:
        messagebox.showerror("City Not Found", "City not found, please enter a valid city.")
# Create the main window
window = tk.Tk()
window.title("Weather Forecast App")
window.geometry("400x300")
# Create input field for city name
city_label = tk.Label(window, text="Enter City Name:")
city_label.pack(pady=10)
city_entry = tk.Entry(window, width=30)
city_entry.pack(pady=5)
# Create a button to get the weather
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)
# Create labels to display the weather data
temp_label = tk.Label(window, text="Temperature: --")
temp_label.pack(pady=5)
pressure_label = tk.Label(window, text="Pressure: --")
pressure_label.pack(pady=5)
humidity_label = tk.Label(window, text="Humidity: --")
humidity_label.pack(pady=5)
description_label = tk.Label(window, text="Description: --")
description_label.pack(pady=5)
# Run the application
window.mainloop()
