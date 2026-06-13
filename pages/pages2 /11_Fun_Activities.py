import streamlit as st

st.set_page_config(page_title="Fun Activities", page_icon="🎾")

st.title("🎾 Fun Activities for Pets")

# Session State
if "my_plans" not in st.session_state:
    st.session_state.my_plans = []

# Activity Data
activities = [
    {
        "name": "Paws Park",
        "type": "Parks",
        "city": "Hyderabad",
        "pet_type": "Dog",
        "address": "Jubilee Hills, Hyderabad",
        "timing": "6 AM - 8 PM",
        "fee": "₹50"
    },
    {
        "name": "Splash Pets",
        "type": "Swimming",
        "city": "Hyderabad",
        "pet_type": "Dog",
        "address": "Gachibowli, Hyderabad",
        "timing": "8 AM - 6 PM",
        "fee": "₹300"
    },
    {
        "name": "Agility Zone",
        "type": "Agility",
        "city": "Bangalore",
        "pet_type": "Dog",
        "address": "Indiranagar, Bangalore",
        "timing": "7 AM - 7 PM",
        "fee": "₹250"
    },
    {
        "name": "Pet Friends Meetup",
        "type": "Playdates",
        "city": "Mumbai",
        "pet_type": "Cat",
        "address": "Andheri West, Mumbai",
        "timing": "5 PM - 8 PM",
        "fee": "Free"
    },
    {
        "name": "Paws Cafe",
        "type": "Pet Cafes",
        "city": "Hyderabad",
        "pet_type": "All",
        "address": "Banjara Hills, Hyderabad",
        "timing": "10 AM - 10 PM",
        "fee": "₹100"
    }
]

# Filters
st.sidebar.header("Filters")

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All", "Hyderabad", "Mumbai", "Bangalore"]
)

selected_pet = st.sidebar.selectbox(
    "Pet Type",
    ["All", "Dog", "Cat", "Bird", "Rabbit"]
)

selected_activity = st.sidebar.selectbox(
    "Activity Type",
    ["All", "Parks", "Swimming", "Agility", "Playdates", "Pet Cafes"]
)

st.subheader("📍 Available Activities")

found = False

for activity in activities:

    city_match = selected_city == "All" or activity["city"] == selected_city
    pet_match = (
        selected_pet == "All"
        or activity["pet_type"] == selected_pet
        or activity["pet_type"] == "All"
    )
    activity_match = (
        selected_activity == "All"
        or activity["type"] == selected_activity
    )

    if city_match and pet_match and activity_match:

        found = True

        st.markdown(f"### {activity['name']}")
        st.write(f"🎯 Activity: {activity['type']}")
        st.write(f"📍 Address: {activity['address']}")
        st.write(f"🕒 Timing: {activity['timing']}")
        st.write(f"💰 Entry Fee: {activity['fee']}")

        if st.button(
            f"➕ Add to My Plans",
            key=activity["name"]
        ):
            if activity["name"] not in st.session_state.my_plans:
                st.session_state.my_plans.append(activity["name"])
                st.success(
                    f"{activity['name']} added to your plans!"
                )

        st.divider()

if not found:
    st.warning("No activities found.")

# My Plans Section
st.subheader("📅 My Plans")

if st.session_state.my_plans:
    for plan in st.session_state.my_plans:
        st.write(f"✅ {plan}")
else:
    st.info("No activities added yet.")
