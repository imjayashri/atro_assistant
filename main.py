
import streamlit as st
from agent import ask_astrology_agent

st.title("🔮 Personal Astrology Assistant")
sign = st.selectbox("Select your Zodiac Sign", [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
])

if st.button("Get My Horoscope"):
    with st.spinner("Consulting the stars..."):
        query = f"What is the horoscope for {sign} today?"
        result = ask_astrology_agent(query)
        st.success(result)
