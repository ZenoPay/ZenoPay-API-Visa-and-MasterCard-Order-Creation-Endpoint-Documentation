import requests

url = "https://zenoapi.com/api/payments/orders/create/"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "YOUR_API_KEY"
}
payload = {
    "order_id": "85ghxdsKLKJKkdnkjknkjhsdsdsddsdkjnLJLKls8",
    "buyer_email": "john@example.com",
    "buyer_name": "John Joh",
    "buyer_phone": "0652449389",
    "amount": 1000,
    "currency": "TZS",
    "payment_methods": "CARD",
    "billing.firstname": "John",
    "billing.lastname": "Doe",
    "billing.phone": "255xxxxxxxxx",
    "status": "pending",
    "no_of_items": 3
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
