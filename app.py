import streamlit as st
import time

# Set page title and icon
st.set_page_config(
    page_title="UniPaw Converter 🐾",
    page_icon="🐾",
    layout="centered"
)

# Custom CSS for enhanced UI
st.markdown(
    

""" <style>
    /* Pink background for the entire app */
    body {
        background-color: #FFC5D3 !important;
    }
    /* Ensure text is readable on pink background */
    .stApp {
        background-color: #FFC5D3;
        color: #000000 !important; /* Black text for all general text */
    }
    /* Style for text boxes (input fields, dropdowns, etc.) */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: #FFFFFF !important; 
        color: #000000 !important; /* Black text for input fields */
    }
    /* Style for buttons */
    .stButton button {
        background-color: #FF69B4 !important; /* Pink background for buttons */
        color: white !important; /* White text for buttons */
        border-radius: 12px;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #ff4786 !important; /* Lighter pink on hover */
    }
    /* Style for success messages */
    .stSuccess {
        background-color: #FFFFFF !important; /* White background for success messages */
        color: #FF1493 !important; /* Pink text for success messages */
        padding: 10px;
        border-radius: 10px;
    }
    /* Style for captions (labels like "Select Conversion Type 🛠️", "From 📏", etc.) */
    .stSelectbox label, .stNumberInput label {
        color: #000000 !important; /* Black text for captions */
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True
)

# Title and Description
st.title("UniPaw Converter 🐾✨")
st.subheader("**Convert units effortlessly with UniPaw! 🌟💖**")
st.write("**UniPaw Converter 🐾✨ is your cute and fun unit-changing buddy! No more boring math—just pick, type, and poof! 🎩🔢 Magic conversion done! Fast, easy, and super adorable. 💖🎀 Try it now! 🚀🐾**")

# Conversion Categories
conversion_type = st.selectbox("Select Conversion Type 🛠️", [
    "Length", "Weight", "Temperature", "Area", "Volume", "Speed", "Time", "Energy", "Pressure"
])

# Conversion Functions
def convert_units(value, from_unit, to_unit, conversion_dict):
    return value * (conversion_dict[to_unit] / conversion_dict[from_unit])

def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ("celsius", "fahrenheit"): lambda v: (v * 9/5) + 32,
        ("fahrenheit", "celsius"): lambda v: (v - 32) * 5/9,
        ("celsius", "kelvin"): lambda v: v + 273.15,
        ("kelvin", "celsius"): lambda v: v - 273.15,
        ("fahrenheit", "kelvin"): lambda v: (v - 32) * 5/9 + 273.15,
        ("kelvin", "fahrenheit"): lambda v: (v - 273.15) * 9/5 + 32,
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

# Unit Dictionaries
unit_dicts = {
    "Length": {"meters": 1, "kilometers": 0.001, "centimeters": 100, "inches": 39.37, "feet": 3.281, "miles": 0.000621},
    "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
    "Area": {"square_meters": 1, "square_kilometers": 0.000001, "square_feet": 10.7639, "acres": 0.000247105},
    "Volume": {"liters": 1, "milliliters": 1000, "gallons": 0.264172, "cubic_feet": 0.0353147},
    "Speed": {"m/s": 1, "km/h": 3.6, "mph": 2.237, "knots": 1.944},
    "Time": {"seconds": 1, "minutes": 1/60, "hours": 1/3600, "days": 1/86400},
    "Energy": {"joules": 1, "kilojoules": 0.001, "calories": 0.239, "kWh": 2.7778e-7},
    "Pressure": {"pascals": 1, "bar": 1e-5, "psi": 0.000145, "atm": 9.8692e-6}
}

# Input Fields
value = st.number_input("Enter the value to convert 🔢", value=1.0)
units = unit_dicts.get(conversion_type, {})
if conversion_type == "Temperature":
    from_unit = st.selectbox("From 🌡️", ["celsius", "fahrenheit", "kelvin"])
    to_unit = st.selectbox("To 🌡️", ["celsius", "fahrenheit", "kelvin"])
    result = convert_temperature(value, from_unit, to_unit)
else:
    from_unit = st.selectbox("From 👉", list(units.keys()))
    to_unit = st.selectbox("To 👈", list(units.keys()))
    result = convert_units(value, from_unit, to_unit, units)

# Convert Button
if st.button("Convert ✨"):
    with st.spinner("Converting... 💪"):  
        time.sleep(1)
        st.success("Converted value: {:.4f} {} 🚀".format(result, to_unit))
st.markdown("---")
st.write("©Cpythight All Rights Reserved 🔒✨ Made by Dua Fatima 2025 💻🎨")