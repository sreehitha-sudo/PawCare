import streamlit as st
from datetime import date

st.set_page_config(page_title="Pet Training", page_icon="🎓")

st.title("🎓 Pet Training Center")

# Session State
if "learned_commands" not in st.session_state:
    st.session_state.learned_commands = []

# DIY Training Section
st.header("🐾 DIY Pet Training")

commands = {
    "Sit": [
        "Hold a treat near your pet's nose",
        "Move the treat upward",
        "Wait until your pet sits",
        "Reward immediately"
    ],
    "Stay": [
        "Ask your pet to sit",
        "Show your palm and say 'Stay'",
        "Take a few steps back",
        "Reward if they stay"
    ],
    "Shake": [
        "Ask your pet to sit",
        "Gently lift one paw",
        "Say 'Shake'",
        "Reward and repeat"
    ],
    "Fetch": [
        "Throw a toy",
        "Encourage your pet to retrieve it",
        "Call them back",
        "Reward when returned"
    ]
}

for command, steps in commands.items():

    with st.expander(f"📖 {command}"):

        for i, step in enumerate(steps, start=1):
            st.write(f"{i}. {step}")

        learned = st.checkbox(
            f"Mark '{command}' as Learned",
            key=command
        )

        if learned and command not in st.session_state.learned_commands:
            st.session_state.learned_commands.append(command)

# Progress Tracker
st.header("📈 Training Progress")

progress = len(st.session_state.learned_commands) / len(commands)

st.progress(progress)

st.write(
    f"Completed {len(st.session_state.learned_commands)} "
    f"of {len(commands)} commands"
)

if st.session_state.learned_commands:
    st.success(
        "Learned Commands: "
        + ", ".join(st.session_state.learned_commands)
    )

st.divider()

# Trainer Section
st.header("👨‍🏫 Professional Trainers")

trainers = [
    {
        "name": "Rahul Sharma",
        "speciality": "Obedience Training",
        "rate": "₹800/session",
        "availability": "Mon-Fri"
    },
    {
        "name": "Priya Reddy",
        "speciality": "Puppy Training",
        "rate": "₹1000/session",
        "availability": "Daily"
    },
    {
        "name": "Kiran Patel",
        "speciality": "Agility Training",
        "rate": "₹1200/session",
        "availability": "Weekends"
    }
]

for trainer in trainers:

    st.markdown(f"### {trainer['name']}")
    st.write(f"🎯 Speciality: {trainer['speciality']}")
    st.write(f"💰 Rate: {trainer['rate']}")
    st.write(f"📅 Availability: {trainer['availability']}")
    st.divider()

# Booking Form
st.header("📅 Book a Training Session")

with st.form("trainer_booking"):

    pet_name = st.text_input("Pet Name")

    trainer_name = st.selectbox(
        "Select Trainer",
        [t["name"] for t in trainers]
    )

    session_date = st.date_input(
        "Training Date",
        min_value=date.today()
    )

    time_slot = st.selectbox(
        "Time Slot",
        [
            "09:00 AM",
            "11:00 AM",
            "02:00 PM",
            "04:00 PM",
            "06:00 PM"
        ]
    )

    submit = st.form_submit_button("Book Session")

if submit:

    st.success("✅ Training Session Booked!")

    st.write(f"🐾 Pet: {pet_name}")
    st.write(f"👨‍🏫 Trainer: {trainer_name}")
    st.write(f"📅 Date: {session_date}")
    st.write(f"⏰ Time: {time_slot}")
