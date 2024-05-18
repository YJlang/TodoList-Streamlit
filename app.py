import streamlit as st
import folium
import pandas as pd
from PIL import Image
import json
import requests
from streamlit_folium import folium_static
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Create a navigation menu
st.sidebar.header("네비게이션")
pages = ["현재 날씨", "예보", "소개"]
selected_page = st.sidebar.selectbox("페이지 선택", pages)

# Display the current date and time in the sidebar
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.write("현재 날짜와 시간:", current_time)

# Custom CSS
st.markdown("""
<style>
    .container {
        max-width: 800px;
        margin: 40px auto;
        padding: 20px;
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Add a logo
image = Image.open("logo.png")
st.sidebar.image(image, use_column_width=True)

# Load author information from a JSON file
@st.cache(ttl=3600)  # Cache for 1 hour
def load_author_info():
    with open("author_info.json", encoding='utf-8') as f:
        return json.load(f)

author_info = load_author_info()

# Display author information on the website
st.write("개발자: " + author_info["name"])
st.write("이메일: " + author_info["email"])

# Check if the profile picture path is correct
profile_picture_path = author_info.get("profile_picture", "")
if profile_picture_path and os.path.exists(profile_picture_path):
    st.image(profile_picture_path, use_column_width=True)
else:
    st.error(f"Profile picture not found at {profile_picture_path}")

# Fetch the API key from environment variables
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

if not API_KEY:
    st.error("Error: OpenWeatherMap API key is not set. Please set the API key in the .env file.")
    st.stop()

if selected_page == "현재 날씨":
    st.write("현재 날씨")
    # Create a map of South Korea
    m = folium.Map(location=[37.5, 127.0], zoom_start=6)

    # Load city coordinates and weather data
    try:
        city_data = pd.read_csv("city_coordinates.csv")
    except Exception as e:
        st.error(f"Error loading city coordinates: {str(e)}")
        st.stop()

    # Initialize the weather_data DataFrame with the required columns
    weather_data = pd.DataFrame(columns=["city", "description", "temperature", "humidity", "wind_speed", "latitude", "longitude"])

    for index, row in city_data.iterrows():
        lat, lon = row["latitude"], row["longitude"]
        city_name = row["city"]
        API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "metric"
        }
        try:
            response = requests.get(API_ENDPOINT, params=params)
            data = response.json()
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            # Append the data including latitude and longitude to the DataFrame
            temp_df = pd.DataFrame([{
                "city": city_name,
                "description": weather_description,
                "temperature": temperature,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "latitude": lat,
                "longitude": lon
            }])
            weather_data = pd.concat([weather_data, temp_df], ignore_index=True)
        except Exception as e:
            st.error(f"Failed to retrieve weather data for {city_name}: {str(e)}")

    # Add markers for major cities
    for index, row in weather_data.iterrows():
        folium.Marker(
            [row["latitude"], row["longitude"]],
            popup=f"{row['city']}: {row['description']}, Temp: {row['temperature']}°C"
        ).add_to(m)

    # Display the map using folium_static
    folium_static(m)

elif selected_page == "예보":
    st.write("예보")
    # Display forecast data here
    try:
        forecast_data = pd.read_csv("forecast_data.csv")
        st.write(forecast_data)
    except Exception as e:
        st.error(f"Forecast data could not be loaded: {str(e)}")

else:
    st.write("소개")
    # Display about page content here
    st.write("""
    이 애플리케이션은 현재 날씨와 예보 정보를 제공합니다. 사용자는 사이드바를 통해 원하는 정보를 선택할 수 있습니다.
    
    ### 기능
    - **현재 날씨**: 전국 주요 도시의 현재 날씨를 지도에 표시합니다.
    - **예보**: 주요 도시의 날씨 예보를 표시합니다.
    - **소개**: 애플리케이션의 기능과 정보를 제공합니다.
    
    ### 개발자 정보
    - 이름: 윤준하
    - 이메일: sean111400@naver.com
    """)