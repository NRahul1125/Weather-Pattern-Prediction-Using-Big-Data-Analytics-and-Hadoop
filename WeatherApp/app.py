import streamlit as st
import pandas as pd
import joblib

# Load trained model and features
model = joblib.load("C:\\Users\\Rahul\\Downloads\\weather_model.pkl")
columns = joblib.load("C:\\Users\\Rahul\\Downloads\\model_features.pkl")

st.title("🌤️ Weather Pattern Prediction App")
st.write("Enter the weather conditions below to predict the actual temperature.")

# Dictionary to store user inputs
user_input = {}

# Dynamically create inputs based on expected features
for col in columns:
    if col == 'Apparent Temperature (C)':
        user_input[col] = st.slider(col, -20.0, 50.0, 10.0)
    elif col == 'Humidity':
        user_input[col] = st.slider(col, 0.0, 1.0, 0.5)
    elif col == 'Wind Speed (km/h)':
        user_input[col] = st.slider(col, 0.0, 60.0, 10.0)
    elif col == 'Visibility (km)':
        user_input[col] = st.slider(col, 0.0, 20.0, 10.0)
    elif col == 'Pressure (millibars)':
        user_input[col] = st.slider(col, 980.0, 1050.0, 1013.0)
    elif col == 'Wind Bearing (degrees)':
        user_input[col] = st.slider(col, 0.0, 360.0, 180.0)
    elif col == 'Day':
        user_input[col] = st.slider(col, 1, 31, 15)
    elif col == 'Month':
        user_input[col] = st.slider(col, 1, 12, 6)
    elif col == 'Hour':
        user_input[col] = st.slider(col, 0, 23, 12)
    elif col.startswith("Summary_") or col.startswith("Precip Type_"):
        label = col.replace("Summary_", "").replace("Precip Type_", "")
        user_input[col] = 1 if st.checkbox(label) else 0
    else:
        # For any additional one-hot encoded or unknown columns, set to 0
        user_input[col] = 0

# Convert input to DataFrame and reindex to match model input
input_df = pd.DataFrame([user_input])
input_df = input_df.reindex(columns=columns, fill_value=0)

# Prediction button
if st.button("🔍 Predict Temperature"):
    prediction = model.predict(input_df)[0]
    st.success(f"🌡️ Predicted Temperature: {round(prediction, 2)} °C")
