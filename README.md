# ZenoPay-API-Visa-and-MasterCard-Order-Creation-Endpoint-Documentation



---

## 🔗 Endpoint

**POST** `https://zenoapi.com/api/payments/orders/create/`

### 🔐 Authentication

Use your **API Key** in the request headers:

```
x-api-key: YOUR_API_KEY
```

---

## 📥 Request Body (JSON)

| Field               | Type    | Required | Description                            |
| ------------------- | ------- | -------- | -------------------------------------- |
| `order_id`          | string  | ✅        | Unique ID for the order                |
| `buyer_email`       | string  | ✅        | Email address of the buyer             |
| `buyer_name`        | string  | ✅        | Full name of the buyer                 |
| `buyer_phone`       | string  | ✅        | Buyer's phone number (local format)    |
| `amount`            | float   | ✅        | Amount to be charged                   |
| `currency`          | string  | ✅        | ISO currency code (e.g., TZS)          |
| `payment_methods`   | string  | ✅        | Payment method: `CARD`, `M-PESA`, etc. |
| `billing.firstname` | string  | ✅        | First name on billing info             |
| `billing.lastname`  | string  | ✅        | Last name on billing info              |
| `billing.phone`     | string  | ✅        | Billing phone number in E.164 format   |
| `status`            | string  | ✅        | Default: `pending`                     |
| `no_of_items`       | integer | ✅        | Total number of items in the order     |

---

## 📤 Sample Request

### 🔧 cURL

```bash
curl -X POST https://zenoapi.com/api/payments/orders/create/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{
    "order_id":"85ghxdsKLKJKkdnkjknkjhsdsdsddsdkjnLJLKls8",
    "buyer_email": "john@example.com",
    "buyer_name": "John Joh",
    "buyer_phone": "0652449389",
    "amount":  1000,
    "currency":"TZS",
    "payment_methods":"CARD",
    "billing.firstname" : "John",
    "billing.lastname" : "Doe",
    "billing.phone" : "255xxxxxxxxx",
    "status" : "pending",
    "no_of_items": 3
}'
```

### 🐍 Python (requests)

```python
import requests

url = "https://zenoapi.com/api/payments/orders/create/"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "YOUR_API_KEY"
}
payload = {
    "order_id": "85ghxdsKLKllkhjjnkjJKkdnkjknkjhsdsdsddsdkjnLJLKls8",
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
```

---

## ✅ Sample Success Response

```json
{
  "success": true,
  "message": "Order created successfully",
  "data": {
    "order_id": "85ghxdsKLjkhjkhjkkjhjkKJKkdnkjknkjhsdsdsddsdkjnLJLKls8",
    "reference": "ZENO123456789",
    "status": "pending",
    "amount": 1000,
    "payment_url": "https://zenoapi.com/pay/redirect/ZENO123456789"
  }
}
```

---

## ❗ Error Response Example

```json
{
  "success": false,
  "message": "Invalid API Key"
}
```

---

## 📘 GitHub README Template

Here’s a sample `README.md` for your GitHub repository:

```md
# 🧾 ZenoPay API – Order Creation

This repository contains the integration guide for creating payment orders via the ZenoPay API.

## 📌 Endpoint

**POST** `https://zenoapi.com/api/payments/orders/create/`

### 🔐 Authentication

Add your API key in the header:
```

x-api-key: YOUR\_API\_KEY

````

## 📥 Payload

```json
{
  "order_id": "UNIQUE_ORDER_ID",
  "buyer_email": "user@example.com",
  "buyer_name": "John Doe",
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
````

## 📤 Response

Success:

```json
{
  "success": true,
  "message": "Order created successfully",
  "data": {
    "reference": "ZENO123456789",
    "payment_url": "https://zenoapi.com/pay/redirect/ZENO123456789"
  }
}
```

## 💬 Support

For help, email us at [support@zenoapi.com](mailto:support@zenoapi.com) or WhatsApp us via our [ZenoPay Pro Assistant](https://wa.me/255xxxxxxxxx).

---

## 📜 License

MIT License

```
