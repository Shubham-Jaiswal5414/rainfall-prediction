import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Rainfall Prediction", layout="centered")

# Add a colorful gradient background and translucent containers
page_bg = """
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg,#a8edea 0%, #fed6e3 50%, #f6f3ff 100%);
        background-attachment: fixed;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"] {
        background: rgba(0,0,0,0);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(255,255,255,0.14), rgba(255,255,255,0.04));
        backdrop-filter: blur(6px);
    }
    .block-container {
        background: rgba(255,255,255,0.65);
        border-radius: 12px;
        padding: 1rem 1.5rem;
    }
    .stButton>button {
        background-color: #1f77b4 !important;
        color: white !important;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("Rainfall Prediction System")
st.write("Synthetic rainfall prediction project")

states = ["maharashtra", "kerala", "tamil nadu", "rajasthan", "punjab", "karnataka", "uttar pradesh", "west bengal"]
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

data = []

# Rainfall patterns based on monsoon season
monsoon_months = {"jun", "jul", "aug", "sep"}
winter_months = {"dec", "jan", "feb"}
summer_months = {"mar", "apr", "may"}

# State-specific rainfall multipliers
state_rainfall = {
    "kerala": 1.8,
    "karnataka": 1.6,
    "tamil nadu": 1.4,
    "maharashtra": 1.2,
    "west bengal": 1.3,
    "punjab": 0.6,
    "rajasthan": 0.4,
    "uttar pradesh": 0.8
}

for state in states:
    for month_idx, month in enumerate(months):
        for day_variation in range(5):
            # Base rainfall calculation
            if month in monsoon_months:
                rainfall = 180 + (month_idx % 4) * 20
            elif month in summer_months:
                rainfall = 40 + (month_idx % 3) * 15
            else:
                rainfall = 20 + (month_idx % 2) * 10
            
            # Apply state multiplier
            rainfall = rainfall * state_rainfall[state]
            
            # Add some variation
            rainfall += (day_variation * 5 - 10)
            
            # Temperature based on month
            if month in ["dec", "jan", "feb"]:
                temp = 20 + month_idx % 3
            elif month in ["mar", "apr", "may"]:
                temp = 28 + month_idx % 3
            else:
                temp = 25 + month_idx % 3
            
            # Humidity based on rainfall
            if month in monsoon_months:
                humidity = 80 + (day_variation % 3) * 2
            else:
                humidity = 50 + (day_variation % 3) * 5
            
            # Wind speed
            if month in monsoon_months:
                wind = 15 + month_idx % 5
            else:
                wind = 8 + month_idx % 4
            
            data.append([state, month, temp, humidity, wind, max(0, rainfall)])

df = pd.DataFrame(
    data,
    columns=["state", "month", "avg_temp", "humidity", "wind_speed", "rainfall_mm"]
)

st.subheader("Dataset Preview")
st.dataframe(df.head())

df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded.drop("rainfall_mm", axis=1)
y = df_encoded["rainfall_mm"]

model = LinearRegression()
model.fit(X, y)

st.subheader("Prediction")

state = st.selectbox("State", states)
month = st.selectbox("Month", months)
temp = st.slider("Temperature", 20, 45, 30)
hum = st.slider("Humidity", 30, 90, 60)
wind = st.slider("Wind Speed", 5, 25, 12)

input_df = pd.DataFrame([{
    "state": state,
    "month": month,
    "avg_temp": temp,
    "humidity": hum,
    "wind_speed": wind
}])

input_df = pd.get_dummies(input_df)
input_df = input_df.reindex(columns=X.columns, fill_value=0)

if st.button("Predict"):
    result = model.predict(input_df)[0]
    st.success(f"Predicted Rainfall: {result:.2f} mm")