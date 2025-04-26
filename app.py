import streamlit as st
import pickle
import pandas as pd

# Set page config
st.set_page_config(page_title="IPL Win Predictor", page_icon="🏏", layout="centered")

# Custom CSS for a prettier UI
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .main {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .stButton>button {
            color: white;
            background: #1e90ff;
            padding: 0.75em 1.5em;
            border-radius: 8px;
            border: none;
        }
        h1 {
            color: #1e90ff;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        h2, h3 {
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# IPL Win Predictor Title
st.title("🏏 IPL Win Predictor")

# Load model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Teams and Cities
team = [
    "Sunrisers Hyderabad",
    "Mumbai Indians",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Kings XI Punjab",
    "Chennai Super Kings",
    "Rajasthan Royals",
    "Delhi Capitals"
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

# Input section
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox("Select Batting Team", sorted(team))
    with col2:
        bowling_team = st.selectbox("Select Bowling Team", sorted(team))

    selected_city = st.selectbox("Select Host City", sorted(cities))

    target = st.number_input("🏹 Target Score", min_value=1)

    col3, col4, col5 = st.columns(3)
    with col3:
        score = st.number_input("Current Score", min_value=0)
    with col4:
        overs = st.number_input("Overs Completed", min_value=0.0, format="%.1f")
    with col5:
        wickets = st.number_input("Wickets Lost", min_value=0, max_value=10)

    submitted = st.form_submit_button("Predict Probability")

# Prediction
if submitted:
    if overs == 0:
        st.warning("Overs can't be 0. Please enter valid overs.")
    else:
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left if balls_left != 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_left],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)

        loss = result[0][0]
        win = result[0][1]

        st.success("🎯 Prediction Result")
        st.markdown(f"### 🏏 **{batting_team} Win Probability**: {round(win*100)}%")
        st.markdown(f"### 🎯 **{bowling_team} Win Probability**: {round(loss*100)}%")
