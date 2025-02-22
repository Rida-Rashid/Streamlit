import streamlit as st

# Currency conversion rates (You can update these rates manually or fetch live rates from an API)
conversion_rates = {
    "US Dollar (USD)": 0.0036,   # 1 PKR to USD
    "Indian Rupee (INR)": 0.30,  # 1 PKR to INR
    "Euro (EUR)": 0.0033,        # 1 PKR to EUR
    "British Pound (GBP)": 0.0029, # 1 PKR to GBP
    "UAE Dirham (AED)": 0.013     # 1 PKR to AED
}

# Set page configuration
st.set_page_config(page_title="Currency Converter", page_icon="💰", layout="centered")

# App title
st.title("💰 Currency Converter")

# Input box for price in Pakistani Rupees (PKR)
amount_in_pkr = st.number_input("Enter amount in Pakistani Rupees (PKR)", value=1.0, format="%.2f", min_value=0.0)

# Dropdown to select target currency
target_currency = st.selectbox("Convert to:", list(conversion_rates.keys()))

# Convert currency when button is clicked
if st.button("Convert"):
    converted_amount = amount_in_pkr * conversion_rates[target_currency]
    st.success(f"{amount_in_pkr:.2f} PKR = {converted_amount:.2f} {target_currency}")
