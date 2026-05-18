import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
import tempfile

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Solar Panel Power Prediction",
    page_icon="☀️",
    layout="wide"
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

.metric-card {
    background-color: #161B22;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE SECTION
# =========================================
st.title("☀️ Solar Panel Power Prediction App")

st.markdown("""
Predict solar power generation using a trained Machine Learning Regression Model.
""")

st.markdown("---")

# =========================================
# SIDEBAR
# =========================================
st.sidebar.header("📊 About Project")

st.sidebar.info("""
This project predicts solar panel power generation using machine learning regression models.
""")

# =========================================
# MODEL LOADING
# =========================================
st.header("🤖 Upload Trained Model")

uploaded_model = st.file_uploader(
    "Upload .pkl regression model",
    type=["pkl"]
)

model = None

if uploaded_model is not None:

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pkl") as tmp_file:
            tmp_file.write(uploaded_model.read())
            tmp_path = tmp_file.name

        model = joblib.load(tmp_path)

        st.success("✅ Model loaded successfully!")

    except Exception as e:
        st.error(f"❌ Error loading model: {e}")

# =========================================
# INPUT FEATURES
# =========================================
st.markdown("---")
st.header("📥 Input Features")

col1, col2, col3 = st.columns(3)

with col1:
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=100.0,
        value=25.0
    )

with col2:
    irradiance = st.number_input(
        "Solar Irradiance",
        min_value=0.0,
        max_value=2000.0,
        value=500.0
    )

with col3:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

# =========================================
# PREDICTION
# =========================================
st.markdown("---")

if st.button("⚡ Predict Solar Power"):

    if model is not None:

        try:
            input_data = np.array([
                [temperature, irradiance, humidity]
            ])

            prediction = model.predict(input_data)

            st.success(
                f"⚡ Predicted Solar Power Generation: {prediction[0]:.2f}"
            )

            # =========================================
            # VISUALIZATION
            # =========================================
            chart_data = pd.DataFrame({
                "Feature": [
                    "Temperature",
                    "Irradiance",
                    "Humidity",
                    "Predicted Power"
                ],
                "Value": [
                    temperature,
                    irradiance,
                    humidity,
                    prediction[0]
                ]
            })

            fig = px.bar(
                chart_data,
                x="Feature",
                y="Value",
                text="Value",
                title="Solar Prediction Analysis"
            )

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Prediction Error: {e}")

    else:
        st.warning("⚠️ Please upload a trained .pkl model first.")

# =========================================
# SAMPLE DATA SECTION
# =========================================
st.markdown("---")
st.header("📈 Sample Solar Dataset")

sample_df = pd.DataFrame({
    "Temperature": [20, 25, 30, 35, 40],
    "Irradiance": [400, 500, 700, 850, 1000],
    "Humidity": [60, 55, 50, 45, 40],
    "Power Output": [120, 180, 250, 320, 400]
})

st.dataframe(sample_df, use_container_width=True)

# =========================================
# FOOTER
# =========================================
st.markdown("---")

st.caption("© 2026 Solar Power Prediction App | Built with Streamlit ☀️")

 