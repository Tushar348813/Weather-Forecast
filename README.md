# Weather-Forecast
Weather Forecast App Explanation and Working
The Weather Forecast App created using Python and Tkinter provides a graphical user interface (GUI) to check the current weather in any given city. This application makes use of the OpenWeatherMap API to fetch real-time weather data and display it to the user. Here's a detailed breakdown of how the app works and its components.

1. GUI Setup (tkinter):
The GUI is built using the tkinter library, which is a standard Python library for creating desktop applications. The app features:

City Input Box: This allows the user to input the name of the city for which they want to check the weather.
Weather Information Labels: These labels display details such as temperature, humidity, pressure, and a brief description of the weather.
Submit Button: The user clicks this button to fetch the weather details for the entered city.
2. Core Functionality:
The core functionality of the app is provided by the function get_weather(), which does the following:

City Name Validation:

If the user doesn’t enter a city name and clicks the “Get Weather” button, the app will display an error message asking for a city name using messagebox.showerror().
API Request:

The app sends an HTTP request to the OpenWeatherMap API to fetch weather data.
The base URL for the API is:
http://api.openweathermap.org/data/2.5/weather?
The request is constructed with the following parameters:
q={city}: This is the city name input by the user.
appid={API_KEY}: This is the API key you get after registering on OpenWeatherMap.
units=metric: This ensures that the temperature is returned in Celsius (you can change it to imperial for Fahrenheit).
Example URL after constructing the request:

http://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key&units=metric
Parsing the Response:

The response from the OpenWeatherMap API is in JSON format. After receiving the response, the program checks if the city is valid by looking at the cod field in the response:
If data["cod"] == "404", it means the city was not found, and an error message is displayed.
Otherwise, the relevant weather data is extracted from the response:
Temperature (main["temp"]): Current temperature in Celsius.
Pressure (main["pressure"]): Atmospheric pressure in hPa.
Humidity (main["humidity"]): Humidity percentage.
Description (weather[0]["description"]): A brief description of the weather (e.g., "clear sky").
Display the Weather:

Once the data is fetched, it is displayed on the GUI in the corresponding labels for temperature, pressure, humidity, and description.
3. Error Handling:
If the user enters an invalid city name (or nothing at all), the app shows an error message through the messagebox.showerror() method, which displays a pop-up with an error message like “City not found, please enter a valid city.”
This ensures that the app doesn’t crash and provides a user-friendly way to handle incorrect inputs.
4. Workflow of the App:
Here's how the app works step-by-step:

Start the App: The user launches the app, which opens a Tkinter window titled "Weather Forecast App".
Enter City Name: The user enters a city name into the provided input box.
Get Weather: The user clicks the "Get Weather" button.
API Call: The app makes a request to OpenWeatherMap API with the entered city name.
Display Data: The app fetches the weather data from the API and updates the labels with the temperature, pressure, humidity, and weather description.
Error Handling: If the city is not found or there's an issue with the input, an error message is shown.
5. GUI Components:
City Name Input Box:

This is a text entry box where users type the name of the city whose weather they want to check.
"Get Weather" Button:

This button triggers the weather data retrieval process when clicked. It calls the get_weather() function.
Weather Data Labels:

Temperature: Displays the current temperature in the city (e.g., "Temperature: 22°C").
Pressure: Shows the atmospheric pressure (e.g., "Pressure: 1015 hPa").
Humidity: Shows the humidity level (e.g., "Humidity: 78%").
Description: Provides a brief description of the weather, like "clear sky", "cloudy", etc.
6. API Key:
To get your own API key, follow these steps:

Go to OpenWeatherMap and create a free account.
Once registered, log in and go to your dashboard.
Generate an API key (usually free for basic use).
Replace "YOUR_API_KEY" in the code with your actual key.
Example Usage:
Open the app.
Enter a city name (e.g., "New York").
Click the "Get Weather" button.
View the results: Temperature, pressure, humidity, and weather description will be displayed.
Final Thoughts:
This app is a simple, functional weather forecast tool. While it uses basic weather data (temperature, humidity, etc.), you can expand the functionality to include features like:

Forecast for multiple days.
Wind speed, visibility, and other weather details.
Icons for different weather conditions.
You can also improve the design, adding colors, fonts, and styles to make the app more visually appealing.
