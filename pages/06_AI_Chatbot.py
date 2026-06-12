import streamlit as st

st.title("🤖 AI Chatbot")

st.write(
    "Ask simple pet-care questions and get quick guidance. This demo chatbot gives friendly suggestions "
    "for common pet care topics."
)

# A small set of example questions to make the page interactive.
examples = [
    "How often should I walk my dog?",
    "What food is best for a puppy?",
    "How can I tell if my pet is dehydrated?",
    "What should I do if my pet seems tired?",
]

st.subheader("Try a question")
selected = st.selectbox("Choose an example", [""] + examples)

question = st.text_input("Or type your own question", value=selected)

if question:
    answer = """
    Here is a simple pet-care suggestion:
    - Make sure your pet has fresh water and a calm place to rest.
    - Keep an eye on appetite, energy, and bathroom habits.
    - If symptoms seem severe or sudden, contact a veterinarian right away.
    """

    if "walk" in question.lower() and "dog" in question.lower():
        answer = "Most adult dogs do well with at least 1-2 walks each day, but the right amount depends on age, breed, and energy level."
    elif "food" in question.lower() and "puppy" in question.lower():
        answer = "Puppies usually do best with puppy-specific food that supports growth, and it is a good idea to ask your vet about portion size."
    elif "dehydrated" in question.lower():
        answer = "Signs of dehydration can include dry gums, lethargy, and fewer wet diapers or less urination. Contact a vet if you notice these signs."

    st.success("AI suggestion")
    st.write(answer)
else:
    st.info("Type a question above to get a quick pet-care suggestion.")
