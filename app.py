import streamlit as st

# Configure the app for a wide layout and a clear browser title.
st.set_page_config(
    page_title="PetCare Platform",
    page_icon="🐾",
    layout="wide",
)

# Main homepage content.
st.title("🐾 PetCare Platform")
st.write(
    "Welcome to your simple pet care dashboard. Manage vet visits, shop for pet essentials, "
    "track health records, set reminders, and access emergency support in one place."
)

st.info(
    "This beginner-friendly app brings together all the major pet care tools for a healthier, "
    "happier routine with your pet."
)

# Hero section with a colorful highlight card.
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #fff7d6, #e6f6ff); padding: 18px; border-radius: 16px; border: 1px solid #f0d9a6;">
        <h3 style="margin-top: 0; color: #7a4b00;">Why pet parents love this platform</h3>
        <p style="margin-bottom: 0; color: #3b3b3b;">
            Explore trusted vet options, shop for pet supplies, keep health records handy, set reminders, access emergency tips, and ask the AI chatbot for quick help.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("\n")

# Feature cards for the homepage.
features = [
    ("🏥 Find a Vet", "Search trusted veterinarians near you."),
    ("🛒 Pet Shop", "Browse food, accessories, grooming, and healthcare items."),
    ("📋 Health Records", "Keep vaccination and medical history organized."),
    ("⏰ Reminders", "Never miss a feeding time, medicine, or vet visit."),
    ("🚨 Emergency", "Get quick emergency contacts and first-aid guidance."),
    ("🤖 AI Chatbot", "Ask simple pet-care questions and get helpful suggestions."),
]

columns = st.columns(3)
for index, (title, text) in enumerate(features):
    with columns[index % 3]:
        st.markdown(
            f"""
            <div style="background-color: #f7fbff; border: 1px solid #dbe9f5; border-radius: 12px; padding: 12px; margin-bottom: 12px;">
                <h4 style="margin-top: 0;">{title}</h4>
                <p style="margin-bottom: 0;">{text}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.caption("Use the sidebar to explore the pages available in this platform.")
