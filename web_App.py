# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:13:34 2025

@author: User
"""

import streamlit as st
import numpy as np
import pickle

# Load the trained Gradient Boosting model
with open("gradient_boosting_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
def main():
    st.set_page_config(page_title="Solar Power Prediction", layout="centered")
    st.title("☀️ Solar Power Prediction using Gradient Boosting")
    st.markdown("### Enter environmental parameters to predict power generation")

    with st.form("input_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            distance_to_solar_noon = st.number_input("Distance to Solar Noon", 0.0, 1.0, 0.5)
            temperature = st.number_input("🌡️ Temperature (°F)", min_value=-50, max_value=130, value=70)
            wind_direction = st.number_input("🧭 Wind Direction (degrees)", min_value=0, max_value=360, value=180)
            wind_speed = st.number_input("💨 Wind Speed (mph)", min_value=0.0, max_value=50.0, value=5.0)
            sky_cover = st.slider("☁️ Sky Cover (0-8)", 0, 8, 4)
        
        with col2:
            visibility = st.number_input("👀 Visibility (miles)", min_value=0.0, max_value=50.0, value=10.0)
            humidity = st.slider("💧 Humidity (%)", 0, 100, 50)
            avg_wind_speed = st.number_input("🌬️ Average Wind Speed (mph)", min_value=0.0, max_value=50.0, value=5.0)
            avg_pressure = st.number_input("🌡️ Average Pressure (inHg)", min_value=25.0, max_value=35.0, value=29.9)
        
        submit_button = st.form_submit_button("🚀 Predict Power Generation")
    
    if submit_button:
        input_features = np.array([[distance_to_solar_noon, temperature, wind_direction, wind_speed,
                                     sky_cover, visibility, humidity, avg_wind_speed, avg_pressure]])
        prediction = model.predict(input_features)
        st.success(f"⚡ Predicted Power Generation: {prediction[0]:,.2f} Joules")
        
        st.markdown("### 📊 Prediction Summary")
        st.write("Below are the values you entered:")
        st.json({
            "Distance to Solar Noon": distance_to_solar_noon,
            "Temperature (°F)": temperature,
            "Wind Direction (°)": wind_direction,
            "Wind Speed (mph)": wind_speed,
            "Sky Cover": sky_cover,
            "Visibility (miles)": visibility,
            "Humidity (%)": humidity,
            "Average Wind Speed (mph)": avg_wind_speed,
            "Average Pressure (inHg)": avg_pressure
        })

if __name__ == "__main__":
    main()

 