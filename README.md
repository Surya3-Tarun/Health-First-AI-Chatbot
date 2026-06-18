# Health-First-AI-Chatbot
**HealthFirst AI** is an AI-powered healthcare assistant built with Python, Streamlit, and Google Gemini AI. It provides symptom-based health information, home remedies, first-aid guidance, emergency alerts, BMI calculation, and daily health tips through an interactive chatbot interface.

Project Structure

health_chatbot/
│
├── app.py
├── health_data.py
├── requirements.txt
└── assets/

Step 1: Create Project Folder

Open VS Code Terminal:

mkdir health_chatbot
cd health_chatbot

Create virtual environment:

python -m venv venv

Activate:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

Install Streamlit:

pip install streamlit
Step 2: Create health_data.py
health_data = {
    "fever": {
        "symptoms": "High body temperature, chills, sweating, weakness.",
        "remedy": """
• Drink plenty of water
• Take adequate rest
• Use a cold compress
• Eat light food
        """,
        "first_aid": """
• Monitor temperature regularly
• Stay hydrated
• Avoid heavy physical activity
        """,
        "doctor": "Consult a doctor if fever exceeds 102°F or lasts more than 3 days."
    },

    "cold": {
        "symptoms": "Runny nose, sneezing, sore throat, mild cough.",
        "remedy": """
• Warm fluids
• Honey with warm water
• Steam inhalation
• Proper sleep
        """,
        "first_aid": """
• Stay warm
• Drink fluids
• Gargle with salt water
        """,
        "doctor": "See a doctor if symptoms worsen after a week."
    },

    "headache": {
        "symptoms": "Pain in head, pressure around forehead, sensitivity to light.",
        "remedy": """
• Rest in a quiet room
• Drink water
• Avoid screen time
        """,
        "first_aid": """
• Relax
• Apply cold compress
• Stay hydrated
        """,
        "doctor": "Consult a doctor for severe or recurring headaches."
    },

    "stomach pain": {
        "symptoms": "Abdominal discomfort, cramps, bloating.",
        "remedy": """
• Drink warm water
• Eat bland foods
• Avoid spicy foods
        """,
        "first_aid": """
• Rest
• Hydrate
• Observe symptoms
        """,
        "doctor": "Seek medical help if pain is severe or persistent."
    }
}
Step 3: Create app.py
import streamlit as st
from health_data import health_data

st.set_page_config(
    page_title="HealthFirst Chatbot",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 HealthFirst Chatbot")
st.subheader("General Health Information Assistant")

st.warning(
    "⚠️ This chatbot provides general health information only. "
    "It is not a substitute for professional medical advice."
)

user_input = st.text_input(
    "Enter your symptom:",
    placeholder="Example: fever"
)

if st.button("Get Information"):

    symptom = user_input.lower().strip()

    if symptom in health_data:

        info = health_data[symptom]

        st.success(f"Information for: {symptom.title()}")

        st.markdown("## 🤒 Common Symptoms")
        st.write(info["symptoms"])

        st.markdown("## 🏠 Home Remedies")
        st.write(info["remedy"])

        st.markdown("## 🚑 First Aid Tips")
        st.write(info["first_aid"])

        st.markdown("## 👨‍⚕️ When to See a Doctor")
        st.error(info["doctor"])

    else:
        st.error(
            "Sorry! Information not available for this symptom."
        )
Step 4: Create requirements.txt
streamlit
Step 5: Run the Chatbot

In terminal:

streamlit run app.py

Browser opens automatically.

Features Included

✅ Fever Information
✅ Cold Information
✅ Headache Information
✅ Stomach Pain Information
✅ Home Remedies
✅ First Aid Tips
✅ Doctor Recommendation
✅ Clean Streamlit UI
