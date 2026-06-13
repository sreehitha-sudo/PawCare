import streamlit as st
import random

st.set_page_config(page_title="Pet Food Delivery", page_icon="🍖")

st.title("🍖 Pet Food Delivery")

# Session State Cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Store Data
stores = [
    {
        "store": "Paws Food Hub",
        "delivery_time": "25-35 mins",
        "menu": [
            {"item": "Dog Food Pack", "price": 350},
            {"item": "Cat Food Pack", "price": 300}
        ]
    },
    {
        "store": "Happy Pets Store",
        "delivery_time": "30-40 mins",
        "menu": [
            {"item": "Bird Seed Mix", "price": 150},
            {"item": "Rabbit Food Pack", "price": 220}
        ]
    }
]

st.subheader("Available Stores")

# Display Stores & Menu
for store in stores:

    st.markdown(f"## 🏪 {store['store']}")
    st.write(f"🚚 Delivery Time: {store['delivery_time']}")

    for food in store["menu"]:

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f"**{food['item']}**")
            st.write(f"₹{food['price']}")

        with col2:
            qty = st.number_input(
                f"Qty {food['item']}",
                min_value=1,
                max_value=20,
                value=1,
                key=f"{store['store']}_{food['item']}"
            )

            if st.button(
                f"Add {food['item']}",
                key=f"btn_{store['store']}_{food['item']}"
            ):
                st.session_state.cart.append({
                    "item": food["item"],
                    "price": food["price"],
                    "quantity": qty
                })
                st.success(f"{food['item']} added to cart!")

    st.divider()

# Cart Section
st.subheader("🛒 Cart")

if st.session_state.cart:

    total = 0

    for item in st.session_state.cart:

        subtotal = item["price"] * item["quantity"]
        total += subtotal

        st.write(
            f"{item['item']} × {item['quantity']} = ₹{subtotal}"
        )

    st.markdown(f"### Total: ₹{total}")

    if st.button("Place Order"):

        eta = random.choice([
            "20 mins",
            "25 mins",
            "30 mins",
            "35 mins",
            "40 mins"
        ])

        st.success("✅ Order Placed Successfully!")

        st.info(f"🚚 Estimated Delivery Time: {eta}")

        st.session_state.cart = []

else:
    st.info("Your cart is empty.")
