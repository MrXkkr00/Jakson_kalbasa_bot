import math

import requests
import hashlib
import time


def click_uchun_fun(nomer, summa):
    summa = float(summa)
    nomer = str(nomer)
    merchant_id = '27124'
    service_id = '35339'
    merchant_user_id = '42957'
    secret_key = 'MuqT7dqbgZY19m'

    timestamp = str(int(time.time()))
    digest = hashlib.sha1((timestamp + secret_key).encode('utf-8')).hexdigest()

    # Set headers
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Auth': f'{merchant_user_id}:{digest}:{timestamp}'
    }

    # Request payload
    payload = {
        'service_id': service_id,
        'amount': summa,  # Replace with actual amount
        'phone_number': nomer,  # Replace with actual phone number
        'merchant_trans_id': nomer  # Replace with actual merchant transaction ID
    }

    # Make the POST request
    response = requests.post('https://api.click.uz/v2/merchant/invoice/create', headers=headers, json=payload)

    # Print the response
    # print(response.status_code)
    # print(response.json())
    # print(response.json()["invoice_id"])
    return response.json()["invoice_id"]


def checkinvoice(invoice):
    invoice_id = str(invoice)
    merchant_user_id = "42957"
    secret_key = "MuqT7dqbgZY19m"
    service_id = "35339"
    # invoice_id = "157901286"

    # Unix vaqt tamg'asi (10 raqamli soniya)
    timestamp = str(int(time.time()))

    # Dayjest yaratish
    digest = hashlib.sha1((timestamp + secret_key).encode('utf-8')).hexdigest()

    # Autentifikatsiya sarlavhasi
    auth_header = f"{merchant_user_id}:{digest}:{timestamp}"

    # So'rov URLi
    url = f"https://api.click.uz/v2/merchant/invoice/status/{service_id}/{invoice_id}"

    # So'rov yuborish
    response = requests.get(
        url,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Auth": auth_header,
        },
    )

    # Javobni ko'rsatish
    if response.status_code == 200:
        data = response.json()
        # print("Javob:", response.json())
        return response.json()["status_note"]
    else:
        return response.status_code, response.text


def yaqin_location_fun(lat_1, lon_1, lat_2, lon_2):
    number = math.sqrt(pow(math.fabs(lat_1 - lat_2), 2) + pow(math.fabs(lon_1 - lon_2), 2))
    return round(number, 6)


# print(yaqin_location_fun(1, 1, 2, 2))

