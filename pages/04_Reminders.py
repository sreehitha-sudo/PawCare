import streamlit as st

st.title("Reminders")

r_type = st.selectbox("Reminder Type", ["Feeding", "Medicine", "Grooming", "Vet Visit", "Vaccination"])

r_pet = st.text_input("Pet Name")

r_date = st.date_input("Reminder Date")

r_note = st.text_area("Note (optional)")

if "reminders" not in st.session_state:
    st.session_state.reminders = []

if st.button("Set Reminder"):
    st.session_state.reminders.append({
        "type": r_type,
        "pet": r_pet,
        "date": str(r_date),
        "note": r_note
    })
    st.success("Reminder set!")

if st.session_state.reminders:
    st.subheader("Your Reminders")
    for r in st.session_state.reminders:
        st.write(f"{r['type']} for {r['pet']} on {r['date']}")
