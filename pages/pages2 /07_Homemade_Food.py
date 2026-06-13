import streamlit as st

st.set_page_config(page_title="Homemade Pet Food", page_icon="🍲")

st.title("🍲 Homemade Pet Food Recipes")

# Pet Type Selector
pet_type = st.selectbox(
    "Select Pet Type",
    ["Dog", "Cat", "Bird", "Rabbit"]
)

# Age Group Selector
age_group = st.selectbox(
    "Select Age Group",
    ["Puppy/Kitten", "Adult", "Senior"]
)

st.subheader(f"Recipes for {pet_type} - {age_group}")

# DOG RECIPES
if pet_type == "Dog":
    st.markdown("### 🐶 Chicken & Rice Meal")
    st.write("**Ingredients:**")
    st.write("- Chicken breast")
    st.write("- Rice")
    st.write("- Carrots")
    st.write("- Peas")

    st.write("**Preparation Steps:**")
    st.write("1. Boil chicken until fully cooked.")
    st.write("2. Cook rice separately.")
    st.write("3. Steam carrots and peas.")
    st.write("4. Mix all ingredients and serve.")

# CAT RECIPES
elif pet_type == "Cat":
    st.markdown("### 🐱 Fish Delight")
    st.write("**Ingredients:**")
    st.write("- Tuna or salmon")
    st.write("- Pumpkin")
    st.write("- Water")

    st.write("**Preparation Steps:**")
    st.write("1. Cook fish thoroughly.")
    st.write("2. Mash pumpkin.")
    st.write("3. Mix fish and pumpkin.")
    st.write("4. Let cool before serving.")

# BIRD RECIPES
elif pet_type == "Bird":
    st.markdown("### 🐦 Healthy Seed Mix")
    st.write("**Ingredients:**")
    st.write("- Bird seeds")
    st.write("- Apple pieces")
    st.write("- Carrot pieces")

    st.write("**Preparation Steps:**")
    st.write("1. Wash fruits and vegetables.")
    st.write("2. Chop into small pieces.")
    st.write("3. Mix with bird seeds.")
    st.write("4. Serve fresh.")

# RABBIT RECIPES
elif pet_type == "Rabbit":
    st.markdown("### 🐰 Veggie Bowl")
    st.write("**Ingredients:**")
    st.write("- Lettuce")
    st.write("- Carrot")
    st.write("- Cucumber")

    st.write("**Preparation Steps:**")
    st.write("1. Wash all vegetables.")
    st.write("2. Chop into small pieces.")
    st.write("3. Mix together.")
    st.write("4. Serve immediately.")

st.success("Always consult a veterinarian before changing your pet's diet.")
