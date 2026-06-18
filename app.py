import streamlit as st
import google.generativeai as genai
import random

# =========================
# CONFIG
# =========================
API_KEY = "AIzaSyDUAPYdq3Vn9wMUJjJZ9PtKk3AT5VB4dhA"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="HealthFirst AI",
    page_icon="🩺",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🩺 HealthFirst AI")

menu = st.sidebar.radio(
    "Select Option",
    [
        "AI Health Assistant",
        "BMI Calculator",
        "Health Tips"
    ]
)

# =========================
# BMI CALCULATOR
# =========================
if menu == "BMI Calculator":

    st.title("⚖️ BMI Calculator")

    weight = st.number_input("Weight (kg)", min_value=1.0)
    height = st.number_input("Height (meters)", min_value=0.5)

    if st.button("Calculate BMI"):

        bmi = weight / (height ** 2)

        st.success(f"Your BMI: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("Underweight")
        elif bmi < 25:
            st.success("Normal Weight")
        elif bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Obese")

# =========================
# HEALTH TIPS
# =========================
elif menu == "Health Tips":

    st.title("💡 Daily Health Tips")

    tips = [
        "Drink at least 2-3 liters of water daily.",
        "Walk for 30 minutes every day.",
        "Sleep 7-8 hours every night.",
        "Reduce sugar intake.",
        "Eat fruits and vegetables daily.",
        "Avoid excessive screen time.",
        "Exercise regularly."
    ]

    st.info(random.choice(tips))

# =========================
# AI HEALTH ASSISTANT
# =========================
else:

    st.title("🩺 HealthFirst AI Assistant")

    st.warning(
        "This assistant provides general health information only. "
        "Always consult a healthcare professional for medical advice."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input(
        "Describe your symptoms..."
    )

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        emergency_keywords = [
            "chest pain",
            "difficulty breathing",
            "heart attack",
            "stroke",
            "unconscious",
            "severe bleeding"
        ]

        if any(
            word in user_input.lower()
            for word in emergency_keywords
        ):

            response = """
🚨 EMERGENCY ALERT

Your symptoms may indicate a serious condition.

Please seek immediate medical attention or call emergency services.
"""

        else:

            prompt = f"""
You are a professional health information assistant.

Provide:
1. Possible causes
2. Home remedies
3. First aid tips
4. When to see a doctor

User symptoms:
{user_input}

Important:
Do not provide medical diagnosis.
"""

            try:

                result = model.generate_content(prompt)

                response = result.text

            except Exception as e:

                response = f"Error: {e}"

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response)

    st.markdown("---")
    st.caption("HealthFirst AI | Streamlit + Gemini")
