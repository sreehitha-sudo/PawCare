import streamlit as st
import pandas as pd

st.title("Find a Veterinarian")

city = st.text_input("Enter your city")

specialty = st.selectbox(
    "Specialty",
    ["All", "General", "Surgery", "Dermatology", "Dentistry"],
)

vets = pd.DataFrame({
    "Name": ["Dr. Priya Sharma", "Dr. Ravi Kumar", "Dr. Anita Singh"],
    "City": ["Hyderabad", "Hyderabad", "Secunderabad"],
    "Specialty": ["General", "Surgery", "Dermatology"],
    "Rating": [4.8, 4.6, 4.9],
    "Phone": ["9876543210", "9123456780", "9988776655"],
})

filtered = vets

if city:
    filtered = filtered[filtered["City"].str.contains(city, case=False, na=False)]

if specialty != "All":
    filtered = filtered[filtered["Specialty"] == specialty]

st.dataframe(filtered, use_container_width=True)
