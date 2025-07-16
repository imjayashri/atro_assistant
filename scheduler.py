
import os
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import Client
from astro_tools import get_daily_horoscope

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp = os.getenv("TWILIO_WHATSAPP_NUMBER")
to_whatsapp = os.getenv("MY_WHATSAPP_NUMBER")

client = Client(account_sid, auth_token)

def send_daily_horoscope():
    sign = "Gemini"  # Change as needed
    message = get_daily_horoscope(sign)
    client.messages.create(
        body=f"🌞 Good Morning!\nYour daily horoscope for {sign}:\n{message}",
        from_=from_whatsapp,
        to=to_whatsapp
    )

scheduler = BlockingScheduler()
scheduler.add_job(send_daily_horoscope, 'cron', hour=7, minute=0)
scheduler.start()
