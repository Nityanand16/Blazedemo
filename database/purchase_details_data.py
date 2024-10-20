# purchase_details_data.py

def get_purchase_details():
    #Returns a dictionary with purchase details to be filled in the form.
    return {
        "name": "Nityanand Gupta",
        "address": "Klokkerhojen",
        "city": "Denmark",
        "state": "Copenhagen",
        "zip_code": "2400",
        "card_type": "Visa",  # You can also return the card type index if preferred
        "card_number": "4123567891235678",
        "card_month": "12",
        "card_year": "2025",
        "name_on_card": "Nityanand Gupta"
    }