import requests
import tkinter as tk
from tkinter import messagebox
import sys
import base64
import socket  # For network checks

# The API key is base64 encoded for security reasons. It is decoded at runtime.
ENCODED_KEY = "MDMwNDZmNDQxODBlMTQwOTA1YTVhMWM5MTZhYjdiYTM="
API_KEY = base64.b64decode(ENCODED_KEY).decode()

# Base URL of the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


# Function to fetch weather data from the API
def get_weather_data(city_name):
    params = {
        "q": city_name,  # Name of the city for which weather data is fetched
        "appid": API_KEY,  # API key for authentication
        "units": "metric"  # Use metric units (Celsius, meters/sec)
    }
    try:
        # Make a GET request to the OpenWeatherMap API
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:  # HTTP 200 indicates success
            return response.json()  # Return the JSON response as a dictionary
        else:
            return None  # Return None if the response status is not 200
    except Exception as e:
        # Show error message but allow the program to continue
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")
        return None


# Function to calculate wind direction as a human-readable string
def calculate_wind_direction(degrees):
    directions = [
        "North", "North-East", "East", "South-East",
        "South", "South-West", "West", "North-West"
    ]
    idx = round(degrees / 45) % 8  # Determine the index of the wind direction based on degrees
    return directions[idx]  # Return corresponding wind direction


# Check if an active internet connection is available
def check_internet():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


# Function to display the weather data in the Tkinter application
def display_weather():
    city_name = city_entry.get()
    if not city_name.strip():
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return  # Do not exit, allow user to correct the input

    # Check if the internet connection is available
    if not check_internet():
        messagebox.showerror("Network Error", "No internet connection. Please check and try again!")
        return  # Do not exit, allow user to reconnect

    # Fetch weather data from the OpenWeatherMap API
    weather_data = get_weather_data(city_name)

    if weather_data:
        try:
            # Extract data from the API response
            weather = weather_data["weather"][0]["description"].capitalize()
            temp = weather_data["main"]["temp"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]
            pressure = weather_data["main"]["pressure"]
            visibility = weather_data["visibility"] / 1000  # Convert visibility to kilometers
            wind_speed = weather_data["wind"]["speed"]
            wind_direction_deg = weather_data["wind"]["deg"]
            wind_direction = calculate_wind_direction(wind_direction_deg)

            # Update the labels in the Tkinter interface with the weather information
            weather_label.config(text=f"Weather: {weather}")
            temp_label.config(text=f"Temperature: {temp} °C")
            feels_like_label.config(text=f"Feels Like: {feels_like} °C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            visibility_label.config(text=f"Visibility: {visibility:.2f} km")
            wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
            wind_direction_label.config(text=f"Wind Direction: {wind_direction} ({wind_direction_deg}°)")
        except KeyError:
            # Handle errors in parsing the API response
            messagebox.showerror("Error", "Failed to parse weather data! Please try again.")
    else:
        # Display an error when the city is not found or the API key is invalid
        messagebox.showerror("Error", "City not found or invalid API key!")


# Tkinter UI setup
root = tk.Tk()
root.title("Weather Forecast")  # Set window title
root.geometry("400x450")  # Set window size
root.resizable(False, False)  # Prevent resizing of the window

# UI label for application title
title_label = tk.Label(root, text="Live Weather Forecast", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# UI label, entry box, and button for entering/executing city search
city_label = tk.Label(root, text="Enter city name:", font=("Arial", 12))
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=display_weather)
fetch_button.pack(pady=10)

# Labels to display weather data dynamically
weather_label = tk.Label(root, text="", font=("Arial", 12))
weather_label.pack(pady=5)

temp_label = tk.Label(root, text="", font=("Arial", 12))
temp_label.pack(pady=5)

feels_like_label = tk.Label(root, text="", font=("Arial", 12))
feels_like_label.pack(pady=5)

humidity_label = tk.Label(root, text="", font=("Arial", 12))
humidity_label.pack(pady=5)

pressure_label = tk.Label(root, text="", font=("Arial", 12))
pressure_label.pack(pady=5)

visibility_label = tk.Label(root, text="", font=("Arial", 12))
visibility_label.pack(pady=5)

wind_speed_label = tk.Label(root, text="", font=("Arial", 12))
wind_speed_label.pack(pady=5)

wind_direction_label = tk.Label(root, text="", font=("Arial", 12))
wind_direction_label.pack(pady=5)

# Run the Tkinter main event loop
try:
    root.mainloop()  # Start the Tkinter event loop
except Exception as e:
    # Capture and display unexpected errors during runtime
    messagebox.showerror("Unexpected Error", f"An error occurred: {e}")