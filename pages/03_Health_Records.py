import streamlit as st

st.title("Pet Health Records")

pet_name = st.text_input("Pet Name")

pet_type = st.selectbox("Pet Type", ["Dog", "Cat", "Bird", "Other"])

dob = st.date_input("Date of Birth")
breed = st.text_input("Breed")

weight = st.number_input("Weight (kg)", 0.1, 100.0, step=0.1)

st.subheader("Vaccination Log")

vaccine = st.text_input("Vaccine Name")

vac_date = st.date_input("Date Given")

next_due = st.date_input("Next Due Date")

if st.button("Save Record"):
    st.success(f"Record saved for {pet_name}")

st.write(f"Next vaccination ({vaccine}) due on: {next_due}")
