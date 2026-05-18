# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import joblib
import plotly.express as px
import pandas as pd

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Solar Power Prediction",
    page_icon="☀️",
    layout="centered"
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.stButton>button {
    background-color: #F59E0B;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #D97706;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOAD MODEL
# =========================================
model = joblib.load("model/solar_model.pkl")

# =========================================
# MAIN APP
# =========================================
def main():

    st.title("☀️ Solar Power Prediction using Gradient Boosting")

    st.markdown("""
    ### Enter environmental parameters to predict solar power generation
    """)

    st.markdown("---")

    # =========================================
    # INPUT FORM
    # =========================================
    with st.form("input_form"):

        col1, col2 = st.columns(2)

        with col1:

            distance_to_solar_noon = st.number_input(
                "🌞 Distance to Solar Noon",
                min_value=0.0,
                max_value=1.0,
                value=0.5
            )

            temperature = st.number_input(
                "🌡️ Temperature (°F)",
                min_value=-50,
                max_value=130,
                value=70
            )

            wind_direction = st.number_input(
                "🧭 Wind Direction (degrees)",
                min_value=0,
                max_value=360,
                value=180
            )

            wind_speed = st.number_input(
                "💨 Wind Speed (mph)",
                min_value=0.0,
                max_value=50.0,
                value=5.0
            )

            sky_cover = st.slider(
                "☁️ Sky Cover (0-8)",
                0,
                8,
                4
            )

        with col2:

            visibility = st.number_input(
                "👀 Visibility (miles)",
                min_value=0.0,
                max_value=50.0,
                value=10.0
            )

            humidity = st.slider(
                "💧 Humidity (%)",
                0,
                100,
                50
            )

            avg_wind_speed = st.number_input(
                "🌬️ Average Wind Speed (mph)",
                min_value=0.0,
                max_value=50.0,
                value=5.0
            )

            avg_pressure = st.number_input(
                "🌡️ Average Pressure (inHg)",
                min_value=25.0,
                max_value=35.0,
                value=29.9
            )

        submit_button = st.form_submit_button(
            "🚀 Predict Power Generation"
        )

    # =========================================
    # PREDICTION
    # =========================================
    if submit_button:

        input_features = np.array([[
            distance_to_solar_noon,
            temperature,
            wind_direction,
            wind_speed,
            sky_cover,
            visibility,
            humidity,
            avg_wind_speed,
            avg_pressure
        ]])

        prediction = model.predict(input_features)

        st.success(
            f"⚡ Predicted Power Generation: {prediction[0]:,.2f} Joules"
        )

        st.markdown("---")

        # =========================================
        # PREDICTION SUMMARY
        # =========================================
        st.subheader("📊 Prediction Summary")

        summary_data = {
            "Feature": [
                "Distance to Solar Noon",
                "Temperature",
                "Wind Direction",
                "Wind Speed",
                "Sky Cover",
                "Visibility",
                "Humidity",
                "Average Wind Speed",
                "Average Pressure"
            ],
            "Value": [
                distance_to_solar_noon,
                temperature,
                wind_direction,
                wind_speed,
                sky_cover,
                visibility,
                humidity,
                avg_wind_speed,
                avg_pressure
            ]
        }

        summary_df = pd.DataFrame(summary_data)

        st.dataframe(summary_df, use_container_width=True)

        # =========================================
        # VISUALIZATION
        # =========================================
        fig = px.bar(
            summary_df,
            x="Feature",
            y="Value",
            text="Value",
            title="Environmental Parameters"
        )

        fig.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

        # =========================================
        # JSON OUTPUT
        # =========================================
        st.subheader("📦 JSON Output")

        st.json({
            "Distance to Solar Noon": distance_to_solar_noon,
            "Temperature (°F)": temperature,
            "Wind Direction (°)": wind_direction,
            "Wind Speed (mph)": wind_speed,
            "Sky Cover": sky_cover,
            "Visibility (miles)": visibility,
            "Humidity (%)": humidity,
            "Average Wind Speed (mph)": avg_wind_speed,
            "Average Pressure (inHg)": avg_pressure,
            "Predicted Power Generation": float(prediction[0])
        })

    # =========================================
    # FOOTER
    # =========================================
    st.markdown("---")

    st.caption(
        "© 2026 Solar Power Prediction App | Built with Streamlit ☀️"
    )

# =========================================
# RUN APP
# =========================================
if __name__ == "__main__":
    main()