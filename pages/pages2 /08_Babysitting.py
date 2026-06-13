import streamlit as st
from datetime import date

st.set_page_config(page_title="Pet Babysitting", page_icon="🐾")

st.title("🐾 Pet Babysitting Services")

# Sample sitter data
sitters = [
    {
        "name": "Priya Sharma",
        "rating": 4.8,
        "price": 500,
        "location": "Hyderabad",
        "pet_type": "Dog",
        "contact": "9876543210"
    },
    {
        "name": "Rahul Verma",
        "rating": 4.7,
        "price": 450,
        "location": "Mumbai",
        "pet_type": "Cat",
        "contact": "9876501234"
    },
    {
        "name": "Anjali Reddy",
        "rating": 4.9,
        "price": 600,
        "location": "Hyderabad",
        "pet_type": "Rabbit",
        "contact": "9123456780"
    },
    {
        "name": "Kiran Patel",
        "rating": 4.6,
        "price": 400,
        "location": "Bangalore",
        "pet_type": "Bird",
        "contact": "9988776655"
    }
]

# Filters
st.sidebar.header("Filters")

city_filter = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(list(set(s["location"] for s in sitters)))
)

pet_filter = st.sidebar.selectbox(
    "Pet Type",
    ["All", "Dog", "Cat", "Bird", "Rabbit"]
)

# Display sitter profiles
st.subheader("Available Sitters")

filtered_sitters = []

for sitter in sitters:
    if (city_filter == "All" or sitter["location"] == city_filter) and \
       (pet_filter == "All" or sitter["pet_type"] == pet_filter):

        filtered_sitters.append(sitter)

        with st.container():
            st.markdown(f"### {sitter['name']}")
            st.write(f"⭐ Rating: {sitter['rating']}")
            st.write(f"💰 ₹{sitter['price']} per day")
            st.write(f"📍 {sitter['location']}")
            st.write(f"🐾 Specializes in: {sitter['pet_type']}")
            st.divider()

# Booking Form
st.subheader("📅 Book a Pet Sitter")

if filtered_sitters:

    sitter_names = [s["name"] for s in filtered_sitters]

    with st.form("booking_form"):
        selected_sitter = st.selectbox(
            "Choose a Sitter",
            sitter_names
        )

        start_date = st.date_input(
            "Start Date",
            date.today()
        )

        end_date = st.date_input(
            "End Date",
            date.today()
        )

        pet_name = st.text_input("Pet Name")
        pet_age = st.number_input(
            "Pet Age",
            min_value=0,
            max_value=30
        )

        special_notes = st.text_area(
            "Special Instructions"
        )

        submit = st.form_submit_button("Book Now")

    if submit:
        chosen = next(
            s for s in filtered_sitters
            if s["name"] == selected_sitter
        )

        st.success("✅ Booking Confirmed!")

        st.write(f"**Sitter:** {chosen['name']}")
        st.write(f"**Location:** {chosen['location']}")
        st.write(f"**Pet Name:** {pet_name}")
        st.write(f"**Dates:** {start_date} to {end_date}")
        st.write(f"**Contact:** {chosen['contact']}")

else:
    st.warning("No sitters found for the selected filters.")
