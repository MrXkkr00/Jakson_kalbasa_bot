import requests
import hashlib
import time

# API ulanish ma'lumotlari

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
        return (response.json()["status_note"])
    else:
        return (response.status_code, response.text)





# print(checkinvoice(157901286))
# checkpayment_id(3377477221)


import requests


def get_check_by_invoice(invoice_number):
    # Define the endpoint URL
    api_key = "MuqT7dqbgZY19m"
    api_url = 'https://api.click.uz/'
    url = f"{api_url}/invoices/{invoice_number}/check"

    # Set up the headers for the request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    try:
        # Make the GET request to fetch the check details
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.json()
        else:
            # Handle unsuccessful request
            print(f"Failed to retrieve check. Status code: {response.status_code}")
            return None
    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")
        return None


# Example usage
invoice_number = "157901286"
# api_url = "https://api.example.com"  # Replace with your actual API URL
# api_key = "your_api_key_here"  # Replace with your actual API key

check_details = get_check_by_invoice(invoice_number)
if check_details:
    print("Check Details:", check_details)
else:
    print("Failed to retrieve check details.")
