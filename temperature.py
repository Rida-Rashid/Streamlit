import streamlit as st

# Set page configuration
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️", layout="centered")

# App title
st.title("🌡️ Temperature Converter")

# Temperature input
temp_input = st.number_input("Enter Temperature Value", value=0.0, format="%.2f")

# Dropdowns for selecting conversion
from_unit = st.selectbox("Convert From", ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.selectbox("Convert To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

# Convert temperature when button is clicked
if st.button("Convert"):
    result = convert_temperature(temp_input, from_unit, to_unit)
    st.success(f"Converted Temperature: {result:.2f} {to_unit}")

