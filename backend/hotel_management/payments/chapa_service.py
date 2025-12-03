import uuid
import requests
from django.conf import settings


def chapa_initialize_payment(amount, email, first_name, last_name, phone, tx_ref, return_url, callback_url):
    payload = {
        "amount": str(amount),
        "currency": "ETB",
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone,
        "tx_ref": tx_ref,
        "return_url": return_url,
        "callback_url": callback_url,
        "customization": {
            "title": "ReservationPay",
            "description": "Hotelreservation"
        }
    }

    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(settings.CHAPA_TRANSACTION_URL, json=payload, headers=headers)
    return response.json()


def chapa_verify_payment(tx_ref):
    url = f"{settings.CHAPA_VERIFY_URL}/{tx_ref}"
    headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}

    response = requests.get(url, headers=headers)
    return response.json()
