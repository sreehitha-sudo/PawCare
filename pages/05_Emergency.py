
import streamlit as st

st.title("Emergency Support")

st.error("If your pet is in immediate danger, call a vet NOW.")

st.subheader("Emergency Vet Contacts")

contacts = {
	"Blue Cross Hyderabad": "040-2351-0777",
	"VSPCA Vizag": "0891-255-0124",
	"Cessna Lifeline": "080-2222-3399",
}

for name, num in contacts.items():
	st.write(f"**{name}**: {num}")

st.subheader("Basic First Aid Tips")

with st.expander("Pet is not breathing"):
	st.write("Check the airway, begin pet CPR if trained, and rush to a vet immediately.")

with st.expander("Pet swallowed something toxic"):
	st.write("Do NOT induce vomiting unless instructed by a vet or poison control. Call your vet or an animal poison control hotline with the product/substance name.")

with st.expander("Pet has a deep wound"):
	st.write("Apply gentle pressure with a clean cloth to control bleeding, keep the pet calm and warm, and get to a vet as soon as possible.")

with st.expander("Pet is unconscious"):
	st.write("Keep the pet warm, check breathing and pulse, do not give food or water, and seek emergency veterinary care immediately.")
