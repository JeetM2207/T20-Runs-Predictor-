import streamlit as st
import pickle
import numpy as np
import pandas as pd


teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka',
    'Rising Pune Supergiants', 'Deccan Chargers', 'Royal Challengers Bengaluru', 'Gujarat Titans', 'Lucknow Super Giants',
    'Punjab Kings', 'Delhi Capitals', 'Chennai Super Kings', 'Rajasthan Royals', 'Kings XI Punjab', 'Delhi Daredevils',
    'Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Rising Pune Supergiant', 'Gujarat Lions', 'Mumbai Indians',
    'Sunrisers Hyderabad'
]

cities = [
    'Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele',
    'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill',
    'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Sharjah', 'Guyana', 'Nottingham',
    'Chittagong', 'Southampton', 'Mumbai', 'Mount Maunganui', 'Kolkata', 'Lahore', 'Delhi',
    'Nagpur', 'Cardiff', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts'
]

# Load model pipeline
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

st.title("🏏 T20 Score Predictor")

# Select inputs
batting_team = st.selectbox('Select Batting Team', sorted(teams))
bowling_team = st.selectbox('Select Bowling Team', sorted([t for t in teams if t != batting_team]))
city = st.selectbox('Match City', sorted(cities))

current_score = st.number_input('Current Score', min_value=0)
overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
wickets_left = st.number_input('Wickets Left', min_value=0, max_value=10)
balls_left = st.number_input('Balls Left', min_value=0, max_value=120)
last_five = st.num_
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

