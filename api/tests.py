import os

from django.test import TestCase
from twilio.rest import Client

# Twilio auth ma'lumotlari
ACCOUNT_SID = "ACc1d2eec1f65fb1877dffad77ffd4c543"
AUTH_TOKEN = "46a4342416602dc32ab970b39b4eb1a3"
PHONE_NUMBER = "+15417647889"


def send_sms(to, message):
    # Twilio mijozi
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    try:
        # SMS yuborish
        message = client.messages.create(
            body=message,
            from_=PHONE_NUMBER,
            to=to
        )
        print(f"SMS muvaffaqiyatli yuborildi. SID: {message.sid}")
    except Exception as e:
        print(f"SMS yuborishda xato: {e}")


# Test qilish
send_sms("+998900066639", "Verification Code is: 123456")
