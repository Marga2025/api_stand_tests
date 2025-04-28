# data.py

headers = {
    "Content-Type": "application/json"
}

def get_user_body (first_name):
    return {
        "firstName": first_name,
        "phone": "+1234567890",
        "address": "Calle Falsa 123"
    }