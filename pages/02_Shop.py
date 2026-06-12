import streamlit as st

st.title("Pet Shop")

category = st.selectbox("Category", ["All", "Food", "Accessories", "Grooming", "Healthcare"])

products = {
	"Royal Canin Dog Food 3kg": {"cat": "Food", "price": 1200},
	"Stainless Steel Bowl": {"cat": "Accessories", "price": 350},
	"Pet Shampoo": {"cat": "Grooming", "price": 299},
	"Tick & Flea Spray": {"cat": "Healthcare", "price": 450},
}

if "cart" not in st.session_state:
	st.session_state.cart = []

st.subheader("Products")
for name, info in products.items():
	if category == "All" or info["cat"] == category:
		col1, col2, col3 = st.columns([3, 1, 1])
		with col1:
			st.write(f"**{name}**")
		with col2:
			st.write(f"₹{info['price']}")
		with col3:
			if st.button("Add to Cart", key=name):
				st.session_state.cart.append({"name": name, "price": info["price"]})
				st.success(f"Added {name} to cart")

st.sidebar.subheader("Cart")
if st.session_state.cart:
	total = sum(item["price"] for item in st.session_state.cart)
	for item in st.session_state.cart:
		st.sidebar.write(f"- {item['name']}: ₹{item['price']}")
	st.sidebar.write(f"**Total:** ₹{total}")
else:
	st.sidebar.write("Cart is empty")
