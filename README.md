
# 🌟 Astro Assistant

A personal astrology assistant built with LangChain, Streamlit, and Aztro API. It fetches daily horoscopes and can even send them via WhatsApp daily using Twilio.

## 🧩 Features
- Get daily horoscopes for all 12 zodiac signs
- Streamlit UI for interactive use
- LangChain-powered chatbot integration
- WhatsApp daily delivery using Twilio
- Easily customizable and extendable

## 🚀 Usage

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Set your `.env` variables
Create a `.env` file:
```
OPENAI_API_KEY=your_openai_key
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
MY_WHATSAPP_NUMBER=whatsapp:+91xxxxxxxxxx
```

### 3. Run the Streamlit app
```
streamlit run main.py
```

### 4. Run the WhatsApp scheduler
```
python scheduler.py
```

## 🌐 Deploy
- Deploy Streamlit app on https://streamlit.io/cloud
- Deploy WhatsApp scheduler via https://render.com or https://railway.app

---

Made with 💫 by Jayashri Tirpude
