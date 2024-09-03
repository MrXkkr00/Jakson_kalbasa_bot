import requests
import hashlib
import time


def click_uchun(nomer, summa ):
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

# print(click_uchun('998993321038', 1000))