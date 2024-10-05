import streamlit as st
import requests
import datetime as dt
from huggingface_hub import InferenceClient
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Hugging Face API Key
client = InferenceClient(api_key="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")

# Dictionary mapping land types in Arabic to their English equivalents
land_type_plants_arabic_to_english = {
    "الطين": "Clay",
    "رملية": "Sandy",
    "طميية": "Silty",
    "طينية مختلطة": "Loamy",
    "خثية": "Peaty",
    "طباشيرية": "Chalky",
    "ملحية": "Saline"
}

# Mapping suitable plants for each English land type
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
    print(city , api_key)
    city = "Giza"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("تعذر استرداد البيانات. يرجى التحقق من اسم المدينة أو المحاولة لاحقًا.")
        return None

# Function to convert Unix timestamp to human-readable format
def convert_timestamp(unix_timestamp):
    return dt.datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

# Function to generate recommendations using Hugging Face API
def get_recommendation(plant, weather_desc, location, land_type_english):
    prompt = f"As an agricultural expert, I need to recommend actions to take care of {plant} planted in {location} with the current weather condition being {weather_desc} , with land type: {land_type_english}  Please suggest steps to improve the plant's health and optimize growth."
    #st.write(plant , weather_desc , location , land_type_english)
    #st.write(prompt)
    response = "".join(message.choices[0].delta.content for message in client.chat_completion(
        model="Qwen/Qwen2.5-1.5B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        stream=True,
    ))

    return response

# Streamlit app layout
st.title("تطبيق معلومات الطقس والنباتات بناءً على نوع الأرض")
st.write("اختر نوع الأرض بالعربية، أدخل النبات الذي تقوم بزراعته، وقدم اسم المدينة للحصول على معلومات حول الطقس وتوصيات.")

# Dropdown for selecting land type in Arabic
land_type_arabic = st.selectbox("اختر نوع الأرض", list(land_type_plants_arabic_to_english.keys()))

# Map the Arabic land type input to English
land_type_english = land_type_plants_arabic_to_english.get(land_type_arabic)

# Display suitable plants based on selected land type in English
if land_type_english:
    suitable_plants = land_type_plants[land_type_english]
    st.write(f"**النباتات المناسبة لأرض {land_type_arabic}:** {', '.join(suitable_plants)}")

# Input field for the plant being planted (Arabic input, mapped to English)
plant_arabic = st.text_input("أدخل اسم النبات الذي تقوم بزراعته", "")
plant_english = translator.translate(plant_arabic, src="ar", dest="en").text if plant_arabic else plant_arabic

# Input field for the city name
city = st.text_input("اسم المدينة")
city_english = translator.translate(city, src="ar", dest="en").text if city else ""


# Define your OpenWeatherMap API key
weather_api_key = "bc295a4bc8727b69c6df749ba9cc88be"

# Fetch and display weather data when city is entered
if city:
    data = get_weather_data(city_english, weather_api_key)
    if data:
        # Extract relevant information
        weather_english = data["weather"][0]["description"]
        weather_desc = translator.translate(data["weather"][0]["description"], dest="en").text  # Translating to English for the model
        temp_celsius = kelvin_to_celsius(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        
        # Display the weather information
        st.subheader(f"الطقس في {city}")
        st.write(f"**الظروف الجوية**: {data['weather'][0]['description']}")  # Original Arabic description
        st.write(f"**درجة الحرارة**: {temp_celsius:.2f} درجة مئوية")
        st.write(f"**الرطوبة**: {humidity}%")

        # Generate and display recommendation if plant and weather data are available
        if plant_english:
            print(plant_english , weather_english , city_english , land_type_english)
            recommendation = get_recommendation(plant_english, weather_english, city_english, land_type_english )
            ar_recommendation = weather_desc = translator.translate(recommendation, dest="ar").text
            st.subheader("التوصيات المقترحة")
            st.write(ar_recommendation)