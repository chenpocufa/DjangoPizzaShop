import requests
from django.urls import reverse
# from . import views
from django.conf import settings
from requests.auth import HTTPBasicAuth


class Bepaid:
    # @staticmethod
    def bp_token(self, total_price):
        redirect = reverse('shop:shop-home')
        url = 'https://envo9ugiz6sh.x.pipedream.net/'
        test = 'true'
        if not settings.DEBUG:
            test = 'false'
        payload = {
            "checkout": {
                "version": 2.1,
                "test": test,
                "transaction_type": "payment",
                "attempts": 3,
                "settings": {
                    "success_url": redirect,
                    "decline_url": redirect,
                    "fail_url": redirect,
                    "cancel_url": redirect,
                    "notification_url": redirect,
                    "button_text": "Привязать карту",
                    "button_next_text": "Вернуться в магазин",
                    "language": "ru",
                },
                "order": {
                    "currency": "BYN",
                    "amount": total_price,
                    "description": 'Заказ в перкарне "Печорин"'
                },
            }
        }
        r = requests.post(url, json=payload)
        r.json()

    # def bp_redirect(self):

