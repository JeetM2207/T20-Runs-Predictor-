import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load pipeline
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

st.title("🏏 T20 Score Predictor")

# Input Fields
teams = ['India', 'Australia', 'England', 'South Africa', 'New Zealand', 'Sri Lanka', 'Pakistan', 'Bangladesh']  # you can expand
cities = ['Mumbai', 'Dubai', 'Colombo', 'Melbourne', 'Delhi', 'Sharjah']  # example values

batting_team = st.selectbox('Select Batting Team', sorted(teams))
bowling_team = st.selectbox('Select Bowling Team', sorted([t for t in teams if t != batting_team]))
city = st.selectbox('Match City', sorted(cities))

current_score = st.number_input('Current Score', min_value=0)
overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
wickets_left = st.number_input('Wickets Left', min_value=0, max_value=10)
balls_left = st.number_input('Balls Left', min_value=0, max_value=120)
last_five = st.number_input('Runs in Last 30 Balls', min_value=0)

# Predict button
if st.button('Predict Final Score', key='predict_button'):
    input_df = pd.DataFrame({
    'batting_team': [batting_team],
    'bowling_team': [bowling_team],
    'city': [city],
    'current_score': [current_score],
    'balls_left': [balls_left],
    'wickets_left': [wickets_left],
    'overs': [overs],
    'last_five': [last_five],  
    'crr': [current_score / overs if overs > 0 else 0]   # Add this
})


    predicted_score = int(pipe.predict(input_df)[0])
    st.markdown(f"### 🏁 Predicted Final Score: {predicted_score}")

