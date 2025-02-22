import streamlit as st
from datetime import date

# Set page configuration
st.set_page_config(page_title="Age Calculator", page_icon="📅", layout="centered")

# App title
st.title("📅 Age Calculator App")

# Input: Date of Birth
dob = st.date_input("Select your Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

# Calculate age when button is clicked
if st.button("Calculate Age"):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    # Display age result
    st.success(f"🎉 You are {age} years old!")
