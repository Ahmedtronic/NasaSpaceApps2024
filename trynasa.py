import streamlit as st
import requests
import datetime as dt
from huggingface_hub import InferenceClient


client = InferenceClient(api_key="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")
# Hugging Face API Key
HF_API_KEY = "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"

# Dictionary mapping land types to suitable plants
land_type_plants = {
    "Clay": ["Rice", "Cabbage", "Broccoli"],
    "Sandy": ["Carrots", "Peanuts", "Watermelons"],
    "Silty": ["Lettuce", "Spinach", "Basil"],
    "Loamy": ["Tomatoes", "Peppers", "Cucumbers"],
    "Peaty": ["Cranberries", "Blueberries", "Mint"],
    "Chalky": ["Spinach", "Beets", "Cabbage"],
    "Saline": ["Barley", "Beetroot", "Spinach"]
}

# Function to get weather data from OpenWeatherMap API
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Could not retrieve data. Please check the city name or try again later.")
        return None

# Function to convert Unix timestamp to human-readable format
def convert_timestamp(unix_timestamp):
    return dt.datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

# Function to generate recommendations using Hugging Face API
def get_recommendation(plant, weather_desc, location):
    prompt = f"As an agricultural expert, I need to recommend actions to take care of {plant} planted in {location} with the current weather condition being {weather_desc}. Please suggest steps to improve the plant's health and optimize growth."
    client = InferenceClient(api_key="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")

    response = "".join(message.choices[0].delta.content for message in client.chat_completion(
        model="Qwen/Qwen2.5-1.5B-Instruct",
        messages=[{"role": "user", "content": prompt }],
        max_tokens=500,
        stream=True,
    ))

    return (response)

# Streamlit app layout
st.title("Land Type, Planting, and Weather Information App")
st.write("Select the land type, enter the plant you are growing, and provide a city name to get suitable plants, weather information, and recommendations.")

# Dropdown for selecting land type
land_type = st.selectbox("Select Land Type", list(land_type_plants.keys()))

# Display suitable plants based on selected land type
if land_type:
    suitable_plants = land_type_plants[land_type]
    st.write(f"**Suitable plants for {land_type} soil:** {', '.join(suitable_plants)}")

# Input field for the plant being planted
plant = st.text_input("Enter the plant you are growing", "")

# Input field for the city name
city = st.text_input("City Name")

# Define your OpenWeatherMap API key
weather_api_key = "c98eb50389c22cd88756d85efb8b4df1"

# Fetch and display weather data when city is entered
if city:
    data = get_weather_data(city, weather_api_key)
    if data:
        # Extract relevant information
        weather_desc = data["weather"][0]["description"]
        temp_celsius = kelvin_to_celsius(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        
        # Display the weather information
        st.subheader(f"Weather in {city}")
        st.write(f"**Condition**: {weather_desc}")
        st.write(f"**Temperature**: {temp_celsius:.2f} °C")
        st.write(f"**Humidity**: {humidity}%")

        # Generate and display recommendation if plant and weather data are available
        if plant:
            recommendation = get_recommendation(plant, weather_desc, city)
            st.subheader("Recommended Actions")
            st.write(recommendation)