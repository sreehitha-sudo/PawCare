import streamlit as st

st.set_page_config(page_title="Pet Match", page_icon="❤️")

st.title("❤️ Pet Match")

# Initialize Session State
if "current_profile" not in st.session_state:
    st.session_state.current_profile = 0

if "likes" not in st.session_state:
    st.session_state.likes = []

# Create Your Pet Profile
st.header("🐾 Create Your Pet Profile")

pet_name = st.text_input("Pet Name")
breed = st.text_input("Breed")
age = st.number_input("Age", min_value=0, max_value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
purpose = st.selectbox("Purpose", ["Play", "Breed"])

st.divider()

# Nearby Pets Database
nearby_pets = [
    {
        "name": "Bruno",
        "breed": "Golden Retriever",
        "age": 3,
        "gender": "Male",
        "purpose": "Play",
        "owner": "Rahul",
        "contact": "9876543210"
    },
    {
        "name": "Luna",
        "breed": "Labrador",
        "age": 2,
        "gender": "Female",
        "purpose": "Breed",
        "owner": "Priya",
        "contact": "9876501234"
    },
    {
        "name": "Max",
        "breed": "Beagle",
        "age": 4,
        "gender": "Male",
        "purpose": "Play",
        "owner": "Anjali",
        "contact": "9123456780"
    }
]

st.header("📍 Nearby Pet Profiles")

if st.session_state.current_profile < len(nearby_pets):

    pet = nearby_pets[st.session_state.current_profile]

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"### 🐶 {pet['name']}")
        st.write(f"Breed: {pet['breed']}")
        st.write(f"Age: {pet['age']} years")
        st.write(f"Gender: {pet['gender']}")
        st.write(f"Purpose: {pet['purpose']}")

    with col2:

        if st.button("❤️ Like"):

            st.session_state.likes.append(pet["name"])

            # Simulate mutual match
            if pet["name"] in ["Luna", "Max"]:

                st.success("🎉 It's a Match!")

                st.write(f"👤 Owner: {pet['owner']}")
                st.write(f"📞 Contact: {pet['contact']}")

            st.session_state.current_profile += 1
            st.rerun()

        if st.button("⏭️ Skip"):

            st.session_state.current_profile += 1
            st.rerun()

else:
    st.success("✅ You've viewed all available pet profiles!")

    if st.session_state.likes:
        st.subheader("❤️ Pets You Liked")
        for liked_pet in st.session_state.likes:
            st.write(f"• {liked_pet}")
