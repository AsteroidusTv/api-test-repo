import requests


def create_charge(payload: dict) -> requests.Response:
    return requests.post("https://api.stripe.com/v1/charges", json=payload, timeout=30)
